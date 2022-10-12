#!/usr/bin/env python3

# Python 3.9.5

# 16_resolve_filenames.py

# Purpose: Resolve filenames which are written inappropriately and cause a UnicodeEncodeError.

# Dependencies
import os
import sys

path = 'C:\\Users\\user\\...'
os.chdir(path)

appropriate_filenames = []
filenames = os.listdir(path)

def resolve_filename(filename):
    resolve = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return resolve.decode('latin-1')
  
for filename in filenames:
    try:
        appropriate_filenames.append(filename)
    except UnicodeEncodeError:
        resolved = resolve_filename(filename)
        appropriate_filenames.append(resolved)
        
print(appropriate_filenames)
