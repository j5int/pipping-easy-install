from setuptools import setup
import re
import sys

def get_version():
    VERSIONFILE="pippingeasyinstall/__init__.py"
    initfile_lines = open(VERSIONFILE, "rt").readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name             = 'pipping-easy-install',
    version          = get_version(),
    license          =  'MIT',
    description      = 'Installs Python win32 executable installers using pywinauto.',
    long_description = \
        """
        Installs Python win32 executable installers using pywinauto, hacking the registry first, so they can be installed in to a virtualenv.
        """,
    author           = 'Matthew Hampton',
    author_email     = 'support@sjsoft.com',
    packages         = ['pippingeasyinstall'],
    zip_safe = False,
    install_requires =  ["pywinauto"] if "win" in sys.platform else []
    ,
    keywords         = 'easy_install pip windows',
    url              = 'https://github.com/matthewhampton/warden-installer',
    entry_points     = {
        'console_scripts': [
            'pipping_easy_install = pippingeasyinstall.Installer:main',
        ]
    },
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)