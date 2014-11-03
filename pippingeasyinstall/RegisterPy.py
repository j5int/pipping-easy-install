# -*- encoding: utf-8 -*-
#
# script to register Python 2.0 or later for use with win32all
# and other extensions that require Python registry settings
#
# Adapted by Matt Hampton from a script
# adapted by Ned Batchelder from a script
# written by Joakim Löw for Secret Labs AB / PythonWare
#
# source:
# http://www.pythonware.com/products/works/articles/regpy20.htm

import sys
import os

try:
    from _winreg import *
except:
    pass

# tweak as necessary
version = sys.version[:3]
installpath = sys.prefix
if not installpath.endswith(os.path.sep):
    installpath += os.path.sep

regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (
    installpath, installpath, installpath
)

class RegisterPy(object):

    def __enter__(self):
        self.a_set = False
        self.b_set = False
        self.created = False
        self.is_all_users = None
        try:
            reg = OpenKey(HKEY_CURRENT_USER, regpath)
            self.is_all_users = False
        except EnvironmentError:
            try:
                reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
                self.is_all_users = True
            except EnvironmentError:
                reg = CreateKey(HKEY_CURRENT_USER, regpath)
                self.created = True
                self.is_all_users = False

        try:
            self.prev_values = {
                installkey: "" if self.created else QueryValue(reg, installkey),
                pythonkey: "" if self.created else QueryValue(reg, pythonkey)
            }
            if self.prev_values[installkey].rstrip("\\").lower() != installpath.rstrip("\\").lower():
                SetValue(reg, installkey, REG_SZ, installpath)
                self.a_set = True
                try:
                    if self.prev_values[pythonkey].lower() != pythonpath.lower():
                        SetValue(reg, pythonkey, REG_SZ, pythonpath)
                        self.b_set = True
                except:
                    if self.a_set and not self.created:
                        SetValue(reg, installkey, REG_SZ, self.prev_values[installkey])
                    raise
        finally:
            CloseKey(reg)



    def __exit__(self, exc_type, exc_value, traceback):
        reg = OpenKey(HKEY_LOCAL_MACHINE if self.is_all_users else HKEY_CURRENT_USER, regpath)
        try:
            try:
                if self.a_set and not self.created:
                    SetValue(reg, installkey, REG_SZ, self.prev_values[installkey])
            finally:
                if self.b_set and not self.created:
                    SetValue(reg, pythonkey, REG_SZ, self.prev_values[pythonkey])
        finally:
            CloseKey(reg)

