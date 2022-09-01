#!/usr/bin/env python3

# Python 3.9.5

# 08_list_directory.py

# Purpose: Get the file names and sizes similar to the dir or ls command.

# Dependency
import os

path = '/Users/user/directory'

files = os.listdir(path)
files.sort()

file_counter = 0
total_size_bytes = 0

for file_name in files:
    file_size_bytes = os.path.getsize(os.path.join(path, file_name))
    print("File name:", file_name, "File size:", file_size_bytes, "Byte")
    total_size_bytes = total_size_bytes + file_size_bytes
    file_counter += 1

print("Total files:", file_counter)
print("Total size:", total_size_bytes, "Bytes")
