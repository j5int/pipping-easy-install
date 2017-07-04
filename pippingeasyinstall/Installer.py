import argparse
import shutil
import tempfile
import time
from zipfile import ZipFile
from pippingeasyinstall.Downloader import Downloader, PyPiDownloader
from pippingeasyinstall.RegisterPy import RegisterPy
from pippingeasyinstall import PackageStore
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
        if 'wxPython' in exe:
            #wxPython uses innosetup
            subprocess.check_call([exe,'/SILENT','/NORESTART','/DIR=%s'%os.path.join(sys.prefix,"Lib", "site-packages")])
        else:
            app = application.Application.start('"%s"' % texe)
            if "numpy" in exe:
                # numpy setup is weird
                connect_to_installer = 0
                inst_app = None
                while connect_to_installer < 100:
                    try:
                        inst_app = application.Application.connect(title_re="Setup numpy*")
                        break
                    except Exception:
                        time.sleep(0.1)
                        connect_to_installer += 1
                if inst_app is None:
                    raise RuntimeError('Could not connect to numpy installer')
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


def uninstall_python_module(package_name, cachedir):
    if package_name == 'wxPython':
        python_exe = os.path.join(sys.prefix, 'python.exe')
        if not os.path.exists(python_exe):
            raise Exception("Cannot uninstall wxPython: cannot find python.exe here: %s" % python_exe)
        wx_install_dir = subprocess.check_output([os.path.join(sys.prefix, 'python.exe'), '-c', "import wx; import os; print os.path.abspath(os.path.dirname(os.path.dirname(wx.__file__)))"]).strip()
        uninstall_exe = os.path.join(wx_install_dir, 'unins000.exe')
        if not os.path.exists(uninstall_exe):
            raise Exception('Cannot uninstall python module. Cannot find uninstall exe: %s', uninstall_exe)
        subprocess.check_call([uninstall_exe, '/SILENT', '/NORESTART'])
        return

    uninstall_name = package_name
    install_log = os.path.abspath(os.path.join(sys.prefix, '%s-wininst.log'%uninstall_name))
    if not os.path.exists(install_log):
        # Look for the msi
        version = package_version(package_name)
        urls, dlls = PackageStore.find_package_urls(package_name, version)
        if urls is None:
            urls, dlls = PackageStore.find_package_urls(package_name)
        if urls is not None:
            msi_install = None
            python_version = sys.version[:3]
            for url in urls:
                if url['python_version'] == python_version:
                    if url["packagetype"] == "msi":
                        msi_install = url
                        break
                    elif url['packagetype'] == 'bdist_wininst':
                        if 'uninstall_name' in url:
                            other_install_log = os.path.abspath(os.path.join(sys.prefix, '%s-wininst.log'%url['uninstall_name']))
                            if os.path.exists(other_install_log):
                                install_log = other_install_log
                                uninstall_name = url['uninstall_name']
                                break

            if not os.path.exists(install_log) and msi_install is not None:
                 fname, md5sum = PyPiDownloader().download_file(msi_install['url'], fname=msi_install['filename'], \
                                                                md5_digest=msi_install.get('md5_digest',None), cachedir=cachedir,\
                                                                out=sys.stdout)
                 if fname:
                     subprocess.check_call(['msiexec','/x',fname,'/quiet','/qn','/norestart'])
                     return
        if not os.path.exists(install_log):
            raise Exception('Cannot uninstall python module. Cannot find msi or install log: %s', install_log)

    uninstall_exe = os.path.abspath(os.path.join(sys.prefix, 'Remove%s.exe'%uninstall_name))
    if not os.path.exists(uninstall_exe):
        raise Exception('Cannot uninstall python module. Cannot find uninstall exe: %s', uninstall_exe)

    app = application.Application.start('"%s" -u "%s"' % (uninstall_exe, install_log))

    _press_buttons(app, 'Please confirm', 'Yes', 'OK', next_count=1, finishdialogname='Uninstall Finished!')

def package_version(package):
    if package == 'wxPython':
        python_exe = os.path.join(sys.prefix, 'python.exe')
        if not os.path.exists(python_exe):
            raise Exception("Cannot check for wxPython version: cannot find python.exe here: %s" % python_exe)
        try:
            v = subprocess.check_output([os.path.join(sys.prefix, 'python.exe'), '-c', "import wx; print wx.__version__"], stderr=open(os.devnull, "w")).strip()
            return v
        except Exception:
            return None
    try:
        d = pkg_resources.get_distribution(package)
        return d.version
    except pkg_resources.DistributionNotFound:
        return None

def main():
    for h in logging.getLogger().handlers:
        logging.getLogger().removeHandler(h)

    parser = argparse.ArgumentParser(description='Pipping Easy Install')
    parser.add_argument('packages', nargs='+', help="Stuff to install")
    parser.add_argument('-u', '--uninstall', action='store_true', dest='uninstall', help='Uninstall instead')
    parser.add_argument("-l", "--loglevel", default="info", help="Set logging level",
                          choices=("debug", "info", "warn", "error", "critical"))
    args = parser.parse_args()

    loglevel = getattr(logging, args.loglevel.upper())
    logging.getLogger().setLevel(loglevel)

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
            (exe, md5) = Downloader().download_file(package, os.path.basename(package).split('?')[0].split('#')[0], out=sys.stdout)
        else:
            if '==' in p:
                (package,version) = p.split('==')
            installed_version = package_version(package)

            if args.uninstall:
                if installed_version is None:
                    print 'Package %s is not installed' % (package)
                    continue

                cachedir = os.environ.get('PIP_DOWNLOAD_CACHE', None)
                uninstall_python_module(package, cachedir)

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
                    if dlls:
                        d = pkg_resources.get_distribution(package)
                        if d and getattr(d, 'location', None):
                            for dll, zip, dest in dlls:
                                install_dll(d.location, dll, zip, dest)
                else:
                    if exe.endswith('msi'):
                        print "Installation complete, but package %s not installed.  This is an msi install, so "\
                        "does not support multiple installs in different virtual environments on the same machine -"\
                        "this is probably what has happened"
                    else:
                        print "Installation completed, but package %s not installed!?" % (package_name)

if __name__ == "__main__":
    main()
