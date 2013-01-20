#!/usr/bin/python

import sys
import os
import zipfile

def find_import(file):
    if file.endswith(".py"):
        pyfile = file
        initfile = os.path.join(file[:-3], "__init__.py")
    else:
        pyfile = file + ".py"
        initfile = os.path.join(file, "__init__.py")

    for dir in sys.path:
        if dir.endswith(".egg"):
            if os.path.isdir(dir):
                if os.path.exists(os.path.join(dir, initfile)):
                    return dir + " (dir)"
            else:
                egg = zipfile.ZipFile(dir)
                for name in egg.namelist():
                    if name == pyfile or name == initfile:
                        return dir + " (zipped)"
                egg.close()
        else:
            path = os.path.join(dir, pyfile)
            if os.path.exists(path):
                return path
            path = os.path.join(dir, initfile)
            if os.path.exists(path):
                return path
    return file + " not found"

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Usage: find_import.py <ModuleName>"
    print find_import(sys.argv[1])
