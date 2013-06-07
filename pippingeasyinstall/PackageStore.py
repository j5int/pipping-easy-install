
_packages = {
    "pywin32" : {
        "latest_version" : "218",
        "versions": {
            "218" : {
                "urls" : [
                    {
                        "python_version" : "2.7",
                        "packagetype" : "bdist_wininst",
                        "filename" : "pywin32-218.win32-py2.7.exe",
                        "md5_digest" : "16e178ac18b49fa0d27ba0be90f460af",
                        "url" : "http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20218/pywin32-218.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520218%2F&ts=1369749647&use_mirror=tenet"
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
                ]
            }
        }
    },
    "psutil" : {
        "latest_version" : "0.7.0",
        "versions": {
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
        return _packages[package_name]["versions"][version]['urls']
    return None