import argparse
import subprocess

__author__ = 'matth'

from pippingeasyinstall.Downloader import Downloader, PyPiDownloader
from pippingeasyinstall.RegisterPy import RegisterPy
try:
    from pywinauto import application
except:
    pywinauto = None
import logging
import os
import sys
import pkg_resources

def install_python_module(exe, next_count=3, wait_for_finish=120):
    app = application.Application.start('"%s"' % os.path.abspath(exe))

    logging.info('Waiting for Setup dialog')
    app.Setup.Wait("exists enabled visible ready", timeout=10, retry_interval=1)

    for i in range(next_count):
        logging.info('Waiting for Next button')
        app.Setup.Wait("exists enabled visible ready", timeout=10, retry_interval=1)
        app.Setup.Next.Wait("exists enabled visible ready", timeout=10, retry_interval=1)
        logging.info('Dialog Message: %s', '\n'.join(app.Setup.Static1.Texts() or []))
        logging.info('Pressing Next (%d)', i+1)
        app.Setup.Next.SetFocus().Click()

    logging.info('Waiting for Finish button')
    app.Setup.Wait("exists enabled visible ready", timeout=60, retry_interval=1)
    app.Setup.Finish.Wait("exists enabled visible ready", timeout=120, retry_interval=1)
    logging.info('Dialog Message: %s', '\n'.join(app.Setup.Static1.Texts() or []))
    logging.info('Pressing Finish (%d)', i+1)
    app.Setup.Finish.SetFocus().Click()

    logging.info('Waiting for Dialog to close')
    app.Setup.WaitNot("exists enabled visible ready", timeout=10, retry_interval=1)

def uninstall_python_module(package_name):
    install_log = os.path.abspath(os.path.join(sys.prefix, '%s-wininst.log'%package_name))
    if not os.path.exists(install_log):
        raise Exception('Cannot uninstall python module. Cannot find install log: %s', install_log)

    uninstall_exe = os.path.abspath(os.path.join(sys.prefix, 'Remove%s.exe'%package_name))
    if not os.path.exists(uninstall_exe):
        raise Exception('Cannot uninstall python module. Cannot find uninstall exe: %s', uninstall_exe)

    app = application.Application.start('"%s" -u "%s"' % (uninstall_exe, install_log))

    logging.info('Waiting for Please confirm dialog')
    app['Please confirm'].Wait("exists enabled visible ready", timeout=10, retry_interval=1)
    logging.info('Waiting for Yes button')
    app['Please confirm'].Yes.Wait("exists enabled visible ready", timeout=10, retry_interval=1)
    app['Please confirm'].Yes.SetFocus().Click()

    logging.info('Waiting for Uninstall Finished! dialog')
    app['Uninstall Finished!'].Wait("exists enabled visible ready", timeout=120, retry_interval=1)
    logging.info('Waiting for OK button')
    app['Uninstall Finished!'].OK.Wait("exists enabled visible ready", timeout=10, retry_interval=1)
    app['Uninstall Finished!'].OK.SetFocus().Click()

    logging.info('Waiting for Dialog to close')
    app['Uninstall Finished!'].WaitNot("exists enabled visible ready", timeout=10, retry_interval=1)

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

                (exe, md5) = PyPiDownloader().download_package(
                    package, version=version, out=sys.stdout, cachedir=cachedir)
                package_name = package

        if 'win' in sys.platform and not args.uninstall:
            with RegisterPy():
                install_python_module(exe)
            if package_name:
                installed_version = package_version(package_name)
                if installed_version:
                    print '%s version %s now installed' % (package_name, installed_version)
                else:
                    print "Installation completed, but package %s not installed!?" % (package_name)

if __name__ == "__main__":
    main()
