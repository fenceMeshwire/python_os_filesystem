#!/usr/bin/env python3

# Python 3.9.5

# 20_remove_multiple_files.py

# Purpose: Remove multiple files within a given directory.

# Dependencies
import os
from pathlib import Path

def remove_processed_files(directory):
  for file in os.listdir(os.path.join(Path.home(), directory)):
    os.remove(os.path.join(Path.home(), directory, file))

if __name__ == '__main__':
  directory = 'test_dir'
  remove_processed_files(directory)
