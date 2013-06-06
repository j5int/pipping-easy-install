import argparse

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
    app = application.Application.start(os.path.abspath(exe))

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

def package_version(package):
    try:
        d = pkg_resources.get_distribution(package)
        return d.version
    except pkg_resources.DistributionNotFound:
        return None

def main():
    parser = argparse.ArgumentParser(description='Pipping Easy Install')
    parser.add_argument('packages', nargs='+', help="Stuff to install")
    args = parser.parse_args()

    for p in args.packages:
        package, version = p, None

        package_name = None
        if os.path.exists(package):
            exe = package
        elif package.startswith('http'):
            (exe, md5) = Downloader().download_file(package, os.path.basename(package).split['?'][0].split('#')[0], out=sys.stdout)
        else:
            if '==' in p:
                (package,version) = p.split('==')
            installed_version = package_version(package)
            if installed_version:
                print '%s version %s already installed' % (package, installed_version)
                continue

            (exe, md5) = PyPiDownloader().download_package(
                package, version=version, python_platform='win32', out=sys.stdout)
            package_name = package

        if 'win' in sys.platform:
            with RegisterPy():
                install_python_module(exe)
            if package_name:
                installed_version = package_version(package_name)
                if installed_version:
                    print '%s version %s now installed' % (package_name, installed_version)
                else:
                    print "Installation completed, but package %s not installed!?" % (package_name)
        else:
            print 'Would execute: ' + exe

if __name__ == "__main__":
    main()
