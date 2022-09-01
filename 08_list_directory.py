#!/usr/bin/env python3

# Python 3.9.5

# 08_list_directory.py

# Purpose: Get the file names and sizes similar to the dir or ls command.

# Dependency
import os

path = '/Users/user/directory'

files = os.listdir(path)
files.sort()

dir_counter, file_counter, total_size_bytes = 0, 0, 0

for file_name in files:
    # Determine if the path is a directory
    if os.path.isdir(os.path.join(path, file_name)):
        print("<DIR>\t", file_name)
        dir_counter += 1
    # Determine if the path is a file
    if not os.path.isdir(os.path.join(path, file_name)):
        print("<FILE>\t", file_name)
        file_counter += 1
    file_size_bytes = os.path.getsize(os.path.join(path, file_name))
    total_size_bytes = total_size_bytes + file_size_bytes

print("Total directories:", dir_counter)
print("Total files:", file_counter)
print("Total size:", total_size_bytes, "Bytes")
