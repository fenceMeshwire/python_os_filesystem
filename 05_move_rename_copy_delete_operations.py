#!/usr/bin/env python3

# Python 3.9.7

# 05_move_rename_operations.py

# Dependencies
import os, shutil

abs_dir = 'C:\\Users\\name'
abs_target_dir = 'C:\\Users\\name\\someDir'

file_name = 'file.txt'
new_file_name = 'new_file.txt'

# Create directory and file if the don't exist:
if not os.path.exists(abs_target_dir):
    os.makedirs(abs_target_dir)
    os.chdir(abs_dir)
if not os.path.isfile(file_name):
    os.chdir(abs_dir)
    file = open(file_name, 'w')
    file.close()

# Move operation
os.chdir(abs_dir) # Change working directory
shutil.move(file_name, abs_target_dir) # Move file to directory

# Copy operation
os.chdir(abs_target_dir) # Change working directory
shutil.copy(file_name, abs_dir) # Copy file to directory

# Rename operation
os.chdir(abs_target_dir) # Change working directory
shutil.move(file_name, new_file_name) # Rename file name.

# Copy operation
os.chdir(abs_dir) # Change working directory
shutil.copy(file_name, abs_target_dir) # Copy file to directory

# Delete operation
os.chdir(abs_target_dir) # Change working directory
os.unlink(file_name) # Delete file
