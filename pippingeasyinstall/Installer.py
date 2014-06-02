import argparse
import shutil
import tempfile
import time
from zipfile import ZipFile
from pippingeasyinstall.Downloader import Downloader, PyPiDownloader
from pippingeasyinstall.RegisterPy import RegisterPy
try:
    from pywinauto import application
except:
    application = None

try:
    from pywinauto.findbestmatch import MatchError
except:
    MatchError = None

import logging
import os
import sys
import pkg_resources
import subprocess

__author__ = 'matth'


def get_enabled_button(window, name):
    try:
        if not window.Exists():
            return None
        button = window[name]
        if button.IsVisible() and button.IsEnabled():
            return button
    except MatchError, e:
        pass
    return None

def install_python_module(exe, next_count=3, wait_for_finish=120):
    dir = tempfile.mkdtemp(suffix='pippingeasyinstall')
    texe = os.path.abspath(os.path.join(dir, os.path.basename(exe)))
    shutil.copy(os.path.abspath(exe), texe)
    if exe.endswith('exe'):
        app = application.Application.start('"%s"' % texe)
        if "numpy" in exe:
            # numpy setup is weird
            inst_app = application.Application.connect(title_re="Setup numpy*")
            _press_buttons(inst_app, 'Setup', 'Next','Finish',next_count=next_count)
            app['Numpy super installer Setup: Completed']['Close'].SetFocus().Click()
        else:
            _press_buttons(app, 'Setup', 'Next', 'Finish', next_count=next_count)
    elif exe.endswith('msi'):
        subprocess.check_call(['msiexec','/i',texe,'/quiet','/qn','/norestart'])
    else:
        raise ValueError('pipping-easy-install does not know how to install %s' % exe)

def _press_buttons(app, dialogname, next_name, finish_name, next_count, finishdialogname=None):
    finishdialogname = finishdialogname or dialogname

    logging.info('Waiting for %s dialog', dialogname)
    app[dialogname].Wait("exists enabled visible ready", timeout=10, retry_interval=1)

    i = 0
    while app.windows_():
        next = get_enabled_button(app[dialogname], next_name)
        finish = None
        if next:
            i += 1
            logging.info('Pressing %s (%d)', next_name, i)
            next.SetFocus().Click()

            if i >= next_count:
                finish = get_enabled_button(app[finishdialogname], finish_name)
        else:
            finish = get_enabled_button(app[finishdialogname], finish_name)

        if finish:
            logging.info('Pressing %s', finish_name)
            finish.SetFocus().Click()
            time.sleep(0.5)
        else:
            time.sleep(1)

def install_dll(location, dll, zip, dest):
    dll_fname = dll.split('/')[-1]
    dll_dir=os.path.join(location, dest)
    with ZipFile(zip, 'r') as zipfile:
        dll_data = zipfile.read(dll)
    with open(os.path.join(dll_dir, dll_fname), 'wb') as f:
        f.write(dll_data)


def uninstall_python_module(package_name):
    install_log = os.path.abspath(os.path.join(sys.prefix, '%s-wininst.log'%package_name))
    if not os.path.exists(install_log):
        raise Exception('Cannot uninstall python module. Cannot find install log: %s', install_log)

    uninstall_exe = os.path.abspath(os.path.join(sys.prefix, 'Remove%s.exe'%package_name))
    if not os.path.exists(uninstall_exe):
        raise Exception('Cannot uninstall python module. Cannot find uninstall exe: %s', uninstall_exe)

    app = application.Application.start('"%s" -u "%s"' % (uninstall_exe, install_log))

    _press_buttons(app, 'Please confirm', 'Yes', 'OK', next_count=1, finishdialogname='Uninstall Finished!')

def package_version(package):
    try:
        d = pkg_resources.get_distribution(package)
        return d.version
    except pkg_resources.DistributionNotFound:
        return None

def main():
    parser = argparse.ArgumentParser(description='Pipping Easy Install')
    parser.add_argument('packages', nargs='+', help="Stuff to install")
    parser.add_argument('-u', '--uninstall', action='store_true', dest='uninstall', help='Uninstall instead')
    args = parser.parse_args()

    for p in args.packages:
        package, version = p, None

        package_name = None
        dlls = []
        if os.path.exists(package):
            if args.uninstall:
                raise ValueError('Cannot uninstall from exe: please use package name')
            exe = package
        elif package.startswith('http'):
            if args.uninstall:
                raise ValueError('Cannot uninstall from web url: please use package name')
            (exe, md5) = Downloader().download_file(package, os.path.basename(package).split['?'][0].split('#')[0], out=sys.stdout)
        else:
            if '==' in p:
                (package,version) = p.split('==')
            installed_version = package_version(package)

            if args.uninstall:
                if installed_version is None:
                    print 'Package %s is not installed' % (package)
                    continue

                uninstall_python_module(package)

            else:
                if installed_version:
                    print '%s version %s already installed' % (package, installed_version)
                    continue

                cachedir = os.environ.get('PIP_DOWNLOAD_CACHE', None)

                (exe, md5, dlls) = PyPiDownloader().download_package(
                    package, version=version, out=sys.stdout, cachedir=cachedir)
                package_name = package

        if 'win' in sys.platform and not args.uninstall:
            with RegisterPy():
                install_python_module(exe)
            if package_name:
                installed_version = package_version(package_name)
                if installed_version:
                    print '%s version %s now installed' % (package_name, installed_version)
                    d = pkg_resources.get_distribution(package)
                    if d and getattr(d, 'location', None):
                        for dll, zip, dest in dlls:
                            install_dll(d.location, dll, zip, dest)
                else:
                    print "Installation completed, but package %s not installed!?" % (package_name)

if __name__ == "__main__":
    main()
