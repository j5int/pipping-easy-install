
__author__ = 'matth'

from pippingeasyinstall.RegisterPy import RegisterPy
from pywinauto import application
import logging
import os
import sys, urllib

def download_file(url, file):
    printed_out = 0
    def reporthook(a,b,c):
    # ',' at the end of the line is important!
        progress = min(60, float(a * b) / c * 60)
        if progress > printed_out:
            sys.stdout.write('.'*(progress-printed_out)),
            sys.stdout.flush()
            printed_out = progress
    urllib.urlretrieve(url, file, reporthook)


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

def main():
    assert len(sys.argv)>1
    url = sys.argv[1]
    if len(sys.argv)>2:
        exe = sys.argv[2]
    else:
        exe = os.path.basename(url)

    if not os.path.exists(exe):
        download_file(url, exe)

    with RegisterPy():
        install_python_module(exe)

if __name__ == "__main__":
    main()
