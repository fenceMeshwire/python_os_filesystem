#!/usr/bin/env python3

# Python 3.9.5

# 21_set_working_directory.py

# Dependencies
import os, platform
from pathlib import Path

if os.name == 'nt' or platform.system() == 'Windows':
    path = 'C:\\...\\...'
    os.chdir(path)
if os.name == 'posix' or platform.system() == 'Darwin':
    path = '/home/...'
    os.chdir(path)
    
print('Path changed to:', Path.cwd())
