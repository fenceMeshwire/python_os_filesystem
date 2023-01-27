#!/usr/bin/env python3

# Python 3.9.5

# 22_find_specific_files_in_dir.py

# Dependencies
import os, glob
from pathlib import Path

directory = 'C:\\Users\\...'
os.chdir(directory)
Path.cwd()

file_ending = '.ttf'
affected_files = []

for filename in os.listdir('.'):
    if filename.endswith('.ttf') or filename.endswith('.otf'):
        affected_files.append(filename)

with open('fonts.txt', 'w') as fout:
    for affected_file in affected_files:
        fout.write(affected_file + '\n')
