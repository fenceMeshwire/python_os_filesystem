#!/usr/bin/env python3

# Python 3.9.5

# 00_introductions.py

# Dependencies
import os
from pathlib import Path

path = Path('C:/Windows/system32/')
os.chdir(path)
Path.cwd()

# Get number of files in the current working directory:
number_of_files = len([filename for filename in os.listdir('.') if os.path.isfile(filename)])
print(number_of_files)

# Get the file names:
filenames = [filename for filename in os.listdir('.') if os.path.isfile(filename)]
print(filenames)
