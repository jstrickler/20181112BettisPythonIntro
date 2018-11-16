#!/usr/bin/env python
import os

FOLDER = 'DATA'
FILE_NAME = 'mary.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

print("file path:", file_path)
print(os.path.exists(file_path))

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

# unix absolute
# /foo/bar
# /foo.txt

# Windows absolute
# C:\foo\bar
# \\foo\bar
# C:\foo.txt

# relative
# foo/bar

p1 = "/Users/jstrick/Desktop/py3intro"
p2 = "/Users/jstrick/Desktop/py3intro/sys_module.py"
print(os.path.basename(p1))
print(os.path.basename(p2))
print(os.path.split(p1))
print(os.path.splitext(p2))
base = os.path.basename(p2)
ext = os.path.splitext(base)
print(ext)
