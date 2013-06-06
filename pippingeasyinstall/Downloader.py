import json

__author__ = 'matth'

import sys
import urllib
import os
import hashlib


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
        if out:
            out.write('\n')

class PyPiDownloader(Downloader):

    def download_package(self, package_name, version=None, python_version=None, python_platform=None, cachedir=None, out=None):
        url = 'http://pypi.python.org/pypi/%s/%s/json' % (package_name, version) if version \
            else 'http://pypi.python.org/pypi/%s/json' % (package_name)
        f = urllib.urlopen(url)
        try:
            if f.getcode() == 200:
                package_info = json.loads(f.read())
            else:
                raise Exception("Error getting package %s%s from PyPI. %s (%d)" % (package_name, ' (%s)'%(version) if version else ' (latest)', f.read(), f.getcode()))
        finally:
            f.close()
        python_version = python_version or sys.version[:3]
        if python_platform is None:
            python_platform = sys.platform
        matching_urls = []
        for url in package_info['urls']:
            if url['python_version'] == python_version and \
                    url['packagetype'] in ('bdist_wininst', 'bdist_msi') and \
                    python_platform in url['filename']:
                matching_urls.append(url)
        if not matching_urls:
            raise Exception("Error getting package %s%s from PyPI. No windows installer package found for Python version %s (%s)"
                        % (package_name, ' (%s)'%(version) if version else ' (latest)', python_version, python_platform))
        matching_urls = sorted(matching_urls, key=lambda u: u['packagetype'])
        url = matching_urls[0]

        fname = url['filename']
        if cachedir:
            fname = os.path.join(cachedir, fname)
        if os.path.exists(fname):
            if 'md5_digest' in url:
                with open(fname, 'rb') as f:
                    md5_digest = hashlib.md5(f.read()).hexdigest()
                if md5_digest.lower() != url['md5_digest'].lower():
                    os.remove(fname)
        if os.path.exists(fname):
            return fname

        self.download_file(url['url'], fname, out=out)
        if 'md5_digest' in url:
            with open(fname, 'rb') as f:
                md5_digest = hashlib.md5(f.read()).hexdigest()
            if md5_digest.lower() != url['md5_digest'].lower():
                raise Exception('Failed to download %s. Mismatched md5sum. Expected %s, but is %s.' % (url['url'], url['md5_digest'], md5_digest))
        return fname




if __name__ == "__main__":
    print PyPiDownloader().download_package(
        'zope.interface',
        #version='12.1.0',
        cachedir='/tmp',
        python_platform='win32',
        out=sys.stdout)
