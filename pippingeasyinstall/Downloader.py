import json

__author__ = 'matth'

import sys
import urllib
import os
import hashlib
import ssl
from pippingeasyinstall import PackageStore

class PackageNotFoundException(Exception):
    pass

class Downloader(object):

    def reporthook(self,a,b,c):
        if self.out:
            progress = min(60, int(round(float(a * b) / c * 60)))
            if progress > self.printed_out:
                self.out.write('.'*(progress-self.printed_out)),
                self.out.flush()
                self.printed_out = progress

    def download_file(self, url, fname=None, md5_digest=None, cachedir=None, out=None, verify_ssl=True):

        if fname is None:
            fname = os.path.basename(url.split('?')[0].split('#')[0])

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

        self._download_file(url, fname, out=out, verify_ssl=verify_ssl)

        with open(fname, 'rb') as f:
            actual_md5_digest = hashlib.md5(f.read()).hexdigest()
        if md5_digest:
            if actual_md5_digest.lower() != md5_digest.lower():
                raise Exception('Failed to download %s. Mismatched md5sum. Expected %s, but is %s.' % (url, md5_digest, actual_md5_digest))

        return (fname, actual_md5_digest)

    def _download_file(self, url, fname, out=None, verify_ssl=True):
        self.printed_out = 0
        self.out = out
        if verify_ssl:
            urllib.urlretrieve(url, fname, self.reporthook)
        else:
            urllib.urlretrieve(url, fname, self.reporthook, context=ssl._create_unverified_context())
        if out:
            out.write('\n')

class PyPiDownloader(Downloader):

    def download_package(self, package_name, version=None, python_version=None, python_platform=None, cachedir=None, out=None):
        python_version = python_version or sys.version[:3]
        if python_platform is None:
            python_platform = sys.platform

        if version and PackageStore.has_package_version(package_name, version):
            r = self._download_package_from_local(package_name, version, python_version, python_platform, cachedir, out)
            if r:
                return r
        try:
            (fname, actual_md5_digest) = self._download_package_from_pypi(package_name, version, python_version, python_platform, cachedir, out)
            return (fname, actual_md5_digest, [])
        except PackageNotFoundException, e:
            r = self._download_package_from_local(package_name, version, python_version, python_platform, cachedir, out)
            if r is None:
                raise
            return r

    def _download_package_from_local(self, package_name, version=None, python_version=None, python_platform=None, cachedir=None, out=None):
        urls, dlls = PackageStore.find_package_urls(package_name, version)
        if urls:
            (fname, actual_md5_digest) = self._download_package(urls, package_name, version, python_version, python_platform, cachedir, out)
            downloaded_dlls = []
            for dll in dlls:
                (zip_fname, actual_md5_digest) = self.download_file(dll['url'], fname=None, md5_digest=dll['md5_digest'], cachedir=cachedir, out=out, verify_ssl=dll.get('verify_ssl', True))
                for file in dll['files']:
                    downloaded_dlls.append((file, zip_fname, dll['destination']))

            return (fname, actual_md5_digest, downloaded_dlls)

        return None

    def _download_package_from_pypi(self, package_name, version=None, python_version=None, python_platform=None, cachedir=None, out=None):
        url = 'http://pypi.python.org/pypi/%s/%s/json' % (package_name, version) if version \
            else 'http://pypi.python.org/pypi/%s/json' % (package_name)
        f = urllib.urlopen(url)
        try:
            if f.getcode() == 200:
                package_info = json.loads(f.read())
            else:
                raise PackageNotFoundException("Error getting package %s%s from PyPI. %s (%d)" % (package_name, ' (%s)'%(version) if version else ' (latest)', f.read(), f.getcode()))
        finally:
            f.close()

        return self._download_package(package_info['urls'], package_name, version, python_version, python_platform, cachedir, out)

    def _download_package(self, urls, package_name, version=None, python_version=None, python_platform=None, cachedir=None, out=None, raise_not_found=True):
        matching_urls = []
        for url in urls:
            if url['python_version'] == python_version and \
                    url['packagetype'] in ('bdist_wininst', "msi", "innosetup") and \
                    python_platform in url['filename']:
                matching_urls.append(url)
        if not matching_urls:
            if raise_not_found:
                raise PackageNotFoundException("Error getting package %s%s from PyPI. No windows installer package found for Python version %s (%s)"
                            % (package_name, ' (%s)'%(version) if version else ' (latest)', python_version, python_platform))
            return None
        matching_urls = sorted(matching_urls, key=lambda u: u['packagetype'])

        return self.download_file(matching_urls[0]['url'], fname=matching_urls[0]['filename'], md5_digest=matching_urls[0].get('md5_digest',None), cachedir=cachedir, out=out,
                                  verify_ssl=matching_urls[0].get('verify_ssl', True))




if __name__ == "__main__":

    # print PyPiDownloader().download_package(
    #     'Twisted',
    #     version='11.1.0',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'Twisted',
    #     #version='11.1.0',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'psutil',
    #     version='0.6.1',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    print PyPiDownloader().download_package(
        'py2exe',
        #version='0.6.9',
        cachedir='/tmp',
        python_platform='win32',
        out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'pycairo',
    #     #version='218',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'pywin32',
    #     version='218',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'pywin32',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'zope.interface',
    #     version='4.0.4',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
    # print PyPiDownloader().download_package(
    #     'zope.interface',
    #     cachedir='/tmp',
    #     python_platform='win32',
    #     out=sys.stdout)
