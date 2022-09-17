#!/usr/bin/env python3

# Python 3.9.5

# 11_import_file.py

# Basic concept of importing a file, e.g. a TXT file.

# Dependency
import os

path = 'C:\\...'        # Absolute path, where the file is located.
os.chdir(path)          # Change the current working directory to this path.

file = 'somefile.txt'   # Name of the file, which is to be imported.

# Opening procedure. Instead of printing a line it is also possible to append the 
# content to a data structure list, dictionary, etc.

with open(file, 'r', encoding='utf-8') as file_input:
    try:
        while True:
            line = next(file_input)
            print(line, end='')
    except StopIteration:
        pass

file_input.close()      # Close the input file afterwards.
