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

    def download_file(self, url, fname=None, md5_digest=None, cachedir=None, out=None):

        if cachedir:
            fname = os.path.join(cachedir, fname)

        if os.path.exists(fname):
            if md5_digest:
                with open(fname, 'rb') as f:
                    actual_md5_digest = hashlib.md5(f.read()).hexdigest()
                if actual_md5_digest.lower() != md5_digest.lower():
                    os.remove(fname)
        if os.path.exists(fname):
            return (fname, actual_md5_digest)

        self._download_file(url, fname, out=out)

        with open(fname, 'rb') as f:
            actual_md5_digest = hashlib.md5(f.read()).hexdigest()
        if md5_digest:
            if actual_md5_digest.lower() != md5_digest.lower():
                raise Exception('Failed to download %s. Mismatched md5sum. Expected %s, but is %s.' % (url, md5_digest, actual_md5_digest))

        return (fname, actual_md5_digest)

    def _download_file(self, url, fname, out=None):
        self.printed_out = 0
        self.out = out
        urllib.urlretrieve(url, fname, self.reporthook)
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

        return self.download_file(matching_urls[0]['url'], fname=matching_urls[0]['filename'], md5_digest=matching_urls[0]['md5_digest'], cachedir=cachedir, out=out)




if __name__ == "__main__":
    print PyPiDownloader().download_package(
        'zope.interface',
        #version='12.1.0',
        cachedir='/tmp',
        python_platform='win32',
        out=sys.stdout)
