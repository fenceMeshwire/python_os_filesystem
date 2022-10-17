#!/usr/bin/env python3

# Python 3.9.5

# 18_non_persistant_temporary_file.py

# Dependency
from tempfile import NamedTemporaryFile

with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as tempfile:
    
    tempfile.write('Hello World!\n')
    tempfile.seek(0)
    content = tempfile.read()
    
    print(data)

# The non-persistent temporary file is now deleted.
