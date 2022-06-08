#!/usr/bin/env python3

# Python 3.9.5

# 03_gather_file_information.py

# Dependency
import os

abs_filepath = 'C:\\Windows\\system32\\calc.exe'

os.path.basename(abs_filepath)
os.path.dirname(abs_filepath)
os.path.split(abs_filepath)

dir_name, file = os.path.split(abs_filepath)

print(dir_name)
print(file)
