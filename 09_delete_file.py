#!/usr/bin/env python3

# Python 3.9.5

# 09_delete_file.py

# Dependency
import os

path = 'C:\\Users\\...'
filename = 'test.txt'

os.chdir(path)
if os.path.isfile(filename):
    os.remove(filename)
    print('Filename: %s successfully removed' % filename)
else:
    print('Filename: %s does not exist.' % filename)
