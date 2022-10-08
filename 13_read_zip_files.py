#!/usr/bin/env python3

# Python 3.9.5

# 13_read_zip_files.py

# Dependencies
import bz2
import gzip
import os

# Change current working directory to this directory:
path = 'C:\\Users\\user\\...'
os.chdir(path)

# Read from compressed gz format:
with gzip.open('gzipped.gz', 'rt') as gzipped_file:
  content = gzipped_file.read()
  
# Read from compressed bz2 format:
with bz2.open('bzipped.bz2', 'rt') as bzipped_file:
  content = bzipped_file.read()
