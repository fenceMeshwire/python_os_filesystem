#!/usr/bin/env python3

# Python 3.9.5

# 14_write_bz2_gzip_files.py

# Dependencies
import bz2
import gzip
import os

# Change current working directory to this directory:
path = 'C:\\Users\\user\\...'
os.chdir(path)

# WRITE TO COMPRESSED DATA

content = '.!?abcdefghijklmnopqrstuvwxyz0123456789'

# Write to compressed gz format:
with gzip.open('gzipped.gz', 'wt') as gzipped_file:
  gzipped_file.write(content)
  
# Write to compressed bz2 format:
with bz2.open('bzipped.bz2', 'wt') as bzipped_file:
  bzipped_file.write(content)
