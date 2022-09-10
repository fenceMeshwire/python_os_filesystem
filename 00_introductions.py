#!/usr/bin/env python3

# Python 3.9.5

# 00_introductions.py

# Dependencies
import os
from pathlib import Path

# Change current working directory
path = Path('C:/Windows/system32/')
os.chdir(path)

# Print current working directory
Path.cwd()

# Return the directories and files of the current working directory
os.listdir('.')

# Get number of files in the current working directory:
number_of_files = len([filename for filename in os.listdir('.') if os.path.isfile(filename)])
print(number_of_files)

# Get the file names in the current working directory:
filenames = [filename for filename in os.listdir('.') if os.path.isfile(filename)]
print(filenames)

# Resolve components of an absolute path, e.g. :
path = Path('C:/Windows/system32/notepad.exe')
os.chdir(path)
Path.cwd()

path.anchor   # 'C:\\'
path.name     # 'notepad.exe'
path.stem     # 'notepad'
path.suffix   # '.exe'
path.drive    # 'C:'
