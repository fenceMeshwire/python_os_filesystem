#!/usr/bin/env python3

# Python 3.9.5

# 08_list_directory.py

# Dependency
import os

path = '/Users/user/directory'

files = os.listdir(path)
files.sort()

for name in files:
  print(name)
