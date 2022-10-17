#!/usr/bin/env python3

# Python 3.9.5

# 17_persistant_temporary_file.py

# Dependency
from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t', delete=False, encoding='utf-8') as tempfile:
    print('Name of the temporary file:', tempfile.name)
    tempfile.write('Hello World\n')
    tempfile.seek(0)
    content = tempfile.read()
    print(content)
