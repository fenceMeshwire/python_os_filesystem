#!/usr/bin/env python3

# Python 3.9.5

# 06_walk_dir_tree.py

# Dependency
import os

for dir_name, sub_dirs, file_names in os.walk('/Users/user/OneDrive'):
    print('Current directory: ', dir_name)

    for sub_dir in sub_dirs:
        print('SUB-DIR in DIR:', dir_name, '\n>', sub_dir)
    
    for file_name in file_names:
        print('FILE in DIR:', dir_name, '\n>>', file_name)
       
    print()
