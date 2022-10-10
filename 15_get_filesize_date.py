#!/usr/bin/env python3

# Python 3.9.5

# 15_get_file_size_date.py

import os
import time

path = 'C:\\Users\\user\\test'

# Get the creation time for a directory or file
creation_time = time.ctime(os.path.getmtime(path))
print(creation_time)

# Get the filesize of a directory or file
filesize = os.path.getsize(path)
print(filesize)
