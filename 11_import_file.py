#!/usr/bin/env python3

# Python 3.9.5

# 11_import_file.py

# Dependency
import os

path = 'C:\\...'
os.chdir(path)

file = 'somefile.txt'

with open(file, 'r', encoding='utf-8') as file_input:
    try:
        while True:
            line = next(file_input)
            print(line, end='')
    except StopIteration:
        pass
