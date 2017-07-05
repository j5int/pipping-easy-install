import sys
from os.path import dirname
_packages = {
    "wxPython": {
        "latest_version": "3.0.2.0",
        "versions": {
            "3.0.2.0": {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "innosetup",
                        "filename" : "wxPython3.0-win32-3.0.1.1-py27.exe",
                        "md5_digest" : "c0119e46357dcfc480d50825c64a90c2",
                        "url" : "http://downloads.sourceforge.net/wxpython/wxPython3.0-win32-3.0.2.0-py27.exe",
                        "verify_ssl": False
                    }
                ]
            },
            "3.0.1.1": {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "innosetup",
                        "filename" : "wxPython3.0-win32-3.0.1.1-py27.exe",
                        "md5_digest" : "2488a3b3065530da67e7cebba8b32aac",
                        "url" : "http://downloads.sourceforge.net/wxpython/wxPython3.0-win32-3.0.1.1-py27.exe",
                        "verify_ssl": False
                    }
                ]
            }
        }
    },
    "greenlet": {
        "latest_version": "0.3.2",
        "versions": {
            "0.3.2": {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "greenlet-0.3.2.win32-py2.7.exe",
                        "md5_digest" : "7e5cc074f6eede39a2b833ed772f1b41",
                        "url" : "https://pypi.python.org/packages/2.7/g/greenlet/greenlet-0.3.2.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "cx-Oracle": {
        "latest_version": "5.2",
        "versions": {
            "5.2" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "cx_Oracle-5.2-11g.win32-py2.7-2.exe",
                        "md5_digest" : "94a2b3dd0922f07d613ed1b67a14b48c",
                        "url" : "https://pypi.python.org/packages/2.7/c/cx_Oracle/cx_Oracle-5.2-11g.win32-py2.7-2.exe",
                        "uninstall_name" : "cx_Oracle",
                    }
                ]
            },
            "5.1.3" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "cx_Oracle-5.1.3-11g.win32-py2.7.exe",
                        "md5_digest" : "c4618c499254ff9adf6db581b699e862",
                        "url" : "https://pypi.python.org/packages/2.7/c/cx_Oracle/cx_Oracle-5.1.3-11g.win32-py2.7.exe",
                        "uninstall_name" : "cx_Oracle",
                    }
                ]
            },
            "5.1.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "msi",
                        "filename" : "cx_Oracle-5.1.1-10g.win32-py2.7.msi",
                        "md5_digest" : "a7fd6ec9c66ca59f8c90af8e85a340a2",
                        "url" : "http://downloads.sourceforge.net/cx-oracle/cx_Oracle-5.1.1-10g.win32-py2.7.msi",
                        "verify_ssl": False
                    }
                ]
            }
        }
    },
    "lxml" : {
        "latest_version": "3.4.4",
        "versions": {
            "3.4.4" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "lxml-3.4.4.win32-py2.7.exe",
                        "md5_digest" : "f69924a6a43d992bf91daf8b0cb25db2",
                        "url" : "https://pypi.python.org/packages/2.7/l/lxml/lxml-3.4.4.win32-py2.7.exe"
                    }
                ]
            },
            "3.3.5" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "lxml-3.3.5.win32-py2.7.exe",
                        "md5_digest" : "2c10ce9cab81e0155a019fb6c0c3e2e9",
                        "url" : "https://pypi.python.org/packages/2.7/l/lxml/lxml-3.3.5.win32-py2.7.exe"
                    }
                ]
            },
            "2.3" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "lxml-2.3.win32-py2.7.exe",
                        "md5_digest" : "9c02aae672870701377750121f5a6f84",
                        "url" : "https://pypi.python.org/packages/2.7/l/lxml/lxml-2.3.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "matplotlib": {
        "latest_version": "1.4.3",
        "versions": {
            "1.4.3": {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "matplotlib-1.4.3.win32-py2.7.exe",
                        "md5_digest" : "f43c20480a1673185afefc7d4848a1d2",
                        "url" : "https://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.4.3/windows/matplotlib-1.4.3.win32-py2.7.exe",
                        "verify_ssl": False
                    }
                ]
            },
            "1.1.0": {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "matplotlib-1.1.0.win32-py2.7.exe",
                        "md5_digest" : "38d7caaa4be612b5b9b3cccca5c89aaf",
                        "url" : "http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.1.0/matplotlib-1.1.0.win32-py2.7.exe/download",
                        "verify_ssl": False
                    }
                ]
            }
        }
    },
    "numpy": {
        "latest_version" : "1.9.2",
        "versions" : {
            "1.9.2" : {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "numpy-1.9.2-win32-superpack-python2.7.exe",
                        "md5_digest" : "694e11489cd5340e06d01f19866ecf3b",
                        "url" : "http://sourceforge.net/projects/numpy/files/NumPy/1.9.2/numpy-1.9.2-win32-superpack-python2.7.exe/download",
                        "verify_ssl": False
                    }
                ]
            },
            "1.6.1" : {
                "urls": [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "numpy-1.6.1-win32-superpack-python2.7.exe",
                        "md5_digest" : "9642412608979d50f72413308f0e2444",
                        "url" : "http://sourceforge.net/projects/numpy/files/NumPy/1.6.1/numpy-1.6.1-win32-superpack-python2.7.exe/download",
                        "verify_ssl": False
                    }
                ]
            }
        }

    },
    "pycrypto": {
        "latest_version": "2.6.1",
        "versions": {
            "2.6.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pycrypto-2.6.1.win32-py2.7.exe",
                        "md5_digest" : "1a8cec46705cc83fcd77d24b6c9d079c",
                        "url" : "http://za-download.sjsoft.com/deps/pycrypto-2.6.1.win32-py2.7.exe"
                    }
                ]
            },
            "2.3" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "msi",
                        "filename" : "pycrypto-2.3.win32-py2.7.msi",
                        "md5_digest" : "c3a73b85fb69608966d6d64e00e85cfd",
                        "url" : "http://za-download.sjsoft.com/deps/pycrypto-2.3.win32-py2.7.msi"
                    }
                ]
            }
        }
    },
    "pyodbc" : {
        "latest_version": "2.1.12",
        "versions": {
            "2.1.12" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pyodbc-2.1.12.win32-py2.7.exe",
                        "md5_digest" : "0f426440b165922b1012bb5777952d09",
                        "url" : "http://pyodbc.googlecode.com/files/pyodbc-2.1.12.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "pytidylib": {
        "latest_version": "0.2.4",
        "versions": {
            "0.2.4" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pytidylib-0.2.4.win32.exe",
                        "md5_digest" : "f06755ead3aaff7369d8d4f4ca7610ea",
                        "url" : "http://download.sjsoft.com/opensource/pytidylib-0.2.4.win32.exe"
                    }
                ],
                "dlls" : [
                    {
                        "files": ["bin/tidy.dll"],
                        "destination": dirname(sys.executable),
                        "name": "HTMLTidy",
                        "version" : "060405",
                        "md5_digest" : "3d716c67a4e35c43042b464abbcbea47",
                        "url": "http://prdownloads.sourceforge.net/int64/tidy-060405-dll-fast.zip?download",
                        "verify_ssl": False
                    },
                ]
            },
            "0.2.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pytidylib-0.2.1.win32.exe",
                        "md5_digest" : "ce99b6a4b4ec24cf721a46a7aa84f890",
                        "url" : "http://download.sjsoft.com/opensource/pytidylib-0.2.1.win32.exe"
                    }
                ],
                "dlls" : [
                    {
                        "files": ["bin/tidy.dll"],
                        "destination": dirname(sys.executable),
                        "name": "HTMLTidy",
                        "version" : "060405",
                        "md5_digest" : "3d716c67a4e35c43042b464abbcbea47",
                        "url": "http://prdownloads.sourceforge.net/int64/tidy-060405-dll-fast.zip?download",
                        "verify_ssl": False
                    },
                ]
            }
        }
    },
    "python-ldap" : {
        "latest_version" : "2.4.19",
        "versions": {
            "2.4.19" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "python-ldap-2.4.19.win32-py2.7.exe",
                        "md5_digest" : "026f8da16897d31339f50f166bce2621",
                        "url" : "https://pypi.python.org/packages/2.7/p/python-ldap/python-ldap-2.4.19.win32-py2.7.exe"
                    }
                ]
            },
            "2.4.9" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "python-ldap-2.4.9.win32-py2.7.exe",
                        "md5_digest" : "e8ba435ef2be486d70c16f56c226c60f",
                        "url" : "http://download.sjsoft.com/opensource/python-ldap-2.4.9.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "pywin32" : {
        "latest_version" : "219",
        "versions": {
            "219" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pywin32-219.win32-py2.7.exe",
                        "md5_digest" : "f270e9f88155f649fc1a6c2f85aa128d",
                        "url" : "http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download",
                        "verify_ssl": False
                    }
                ]
            },
            "218" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pywin32-218.win32-py2.7.exe",
                        "md5_digest" : "16e178ac18b49fa0d27ba0be90f460af",
                        "url" : "http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20218/pywin32-218.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520218%2F&ts=1369749647&use_mirror=tenet",
                        "verify_ssl": False
                    }
                ]
            },
            "217" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pywin32-217.win32-py2.7.exe",
                        "md5_digest" : "42202e223b9d21079f397b9116093ac6",
                        "url" : "http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20217/pywin32-217.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520217%2F&ts=1404913990&use_mirror=tenet",
                        "verify_ssl": False
                    }
                ]
            }
        }
    },
    "pycairo" : {
        "latest_version" : "1.8.10",
        "versions": {
            "1.8.10" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pycairo-1.8.10.win32-py2.7.exe",
                        "md5_digest" : "21b17e99f5a606a1e2008067fa5d82ab",
                        "url" : "http://ftp.acc.umu.se/pub/gnome/binaries/win32/pycairo/1.8/pycairo-1.8.10.win32-py2.7.exe"
                    }
                ],
                "dlls" : [
                    {
                        "files": ["bin/zlib1.dll"],
                        "destination": "cairo",
                        "name": "zlib",
                        "version" : "1.2.5",
                        "md5_digest" : "453d63205afcd648f5d6f9ed59f1cc82",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/zlib_1.2.5-2_win32.zip"
                    },
                    {
                        "files": ["bin/libcairo-2.dll", "bin/libcairo-gobject-2.dll", "bin/libcairo-script-interpreter-2.dll"],
                        "destination": "cairo",
                        "name": "cairo",
                        "version" : "1.10.2",
                        "md5_digest" : "97c03ea128f9e3d4e32044a7520b74a9",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/cairo_1.10.2-2_win32.zip"
                    },
                    {
                        "files": ["bin/libpng14-14.dll"],
                        "destination": "cairo",
                        "name": "libpng",
                        "version" : "1.4.3",
                        "md5_digest" : "44ee062641a204f65f0e96720fe57282",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/libpng_1.4.3-1_win32.zip"
                    },
                    {
                        "files": ["bin/freetype6.dll"],
                        "destination": "cairo",
                        "name": "Freetype",
                        "version" : "2.4.2",
                        "md5_digest" : "3087ab1ad08716621fdb43e94f2b3bc1",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/freetype_2.4.2-1_win32.zip"
                    },
                    {
                        "files": ["bin/libfontconfig-1.dll"],
                        "destination": "cairo",
                        "name": "Fontconfig",
                        "version" : "2.8.0",
                        "md5_digest" : "1ec9bc0123bc8b2d9e273272bfeb9795",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/fontconfig_2.8.0-2_win32.zip"
                    },
                    {
                        "files": ["bin/libexpat-1.dll"],
                        "destination": "cairo",
                        "name": "expat",
                        "version" : "2.0.1",
                        "md5_digest" : "99da6bef2cfb051ecda4d70ff24ed149",
                        "url": "http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/expat_2.0.1-1_win32.zip"
                    }
                ]
            }
        }
    },
    "psutil" : {
        "latest_version" : "3.0.1",
        "versions": {
            "3.0.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "psutil-3.0.1.win32-py2.7.exe",
                        "md5_digest" : "38444c787142f33c4f7b0c5cd0a2dedf",
                        "url" : "https://pypi.python.org/packages/2.7/p/psutil/psutil-3.0.1.win32-py2.7.exe"
                    }
                ]
            },
            "0.7.0" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "psutil-0.7.0.win32-py2.7.exe",
                        "md5_digest" : "5696fbc8b2da9603b393f119166a28a1",
                        "url" : "https://psutil.googlecode.com/files/psutil-0.7.0.win32-py2.7.exe"
                    }
                ]
            },
            "0.6.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "psutil-0.6.1.win32-py2.7.exe",
                        "md5_digest" : "8d73121603c0aaf87e0056bd615755f5",
                        "url" : "http://psutil.googlecode.com/files/psutil-0.6.1.win32-py2.7.exe"
                    }
                ]
            },
            "0.4.1" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "psutil-0.4.1.win32-py2.7.exe",
                        "md5_digest" : "aae9ad6b466d3085bab177d3f3859cab",
                        "url" : "https://pypi.python.org/packages/2.7/p/psutil/psutil-0.4.1.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "py2exe" : {
        "latest_version" : "0.6.9",
        "versions": {
            "0.6.9" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "py2exe-0.6.9.win32-py2.7.exe",
                        "md5_digest" : "b7899302e70596defe3b7e8c95cd15c1",
                        "url" : "http://downloads.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpy2exe%2Ffiles%2Fpy2exe%2F0.6.9%2F&ts=1373628132&use_mirror=tenet",
                        "verify_ssl": False
                    }
                ]
            }
        }
    },
    "SendKeys" : {
        "latest_version" : "0.3",
        "versions": {
            "0.3" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "SendKeys-0.3.win32-py2.7.exe",
                        "md5_digest" : "11336eb2347b20490ea233edecd448ed",
                        "url" : "http://web.dyfis.net/SendKeys-0.3.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
    "Twisted" : {
        # For some reason the Twisted bdist_wininst installer for 11.1.0 isn't on PyPI
        "versions": {
            "11.1.0" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "Twisted-11.1.0.win32-py2.7.exe",
                        "md5_digest" : "3815ebb4b60eda48f0b3a240bdceac64",
                        "url" : "http://twistedmatrix.com/Releases/Twisted/11.1/Twisted-11.1.0.win32-py2.7.exe"
                    }
                ]
            }
        }
    },
}



def has_package_version(package_name, version):
    return package_name in _packages and version in _packages[package_name]["versions"]

def find_package_urls(package_name, version=None):
    if package_name in _packages:
        version = version or _packages[package_name]['latest_version']
        return _packages[package_name]["versions"][version]['urls'], _packages[package_name]["versions"][version].get('dlls', [])
    return None, None
