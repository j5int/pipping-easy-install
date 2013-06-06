__author__ = 'matth'

import sys, urllib


class Downloader(object):

    def reporthook(self,a,b,c):
        if self.out:
            progress = min(60, int(round(float(a * b) / c * 60)))
            if progress > self.printed_out:
                self.out.write('.'*(progress-self.printed_out)),
                self.out.flush()
                self.printed_out = progress

    def download_file(self, url, file, out=None):
        self.printed_out = 0
        self.out = out
        urllib.urlretrieve(url, file, self.reporthook)


if __name__ == "__main__":
    Downloader().download_file(
        'http://psutil.googlecode.com/files/psutil-0.6.1.win32-py2.7.exe',
        '/tmp/psutil-0.6.1.win32-py2.7.exe',
        sys.stdout)
