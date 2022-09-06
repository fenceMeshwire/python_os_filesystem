#!/usr/bin/env python3

# Python 3.9.5

# 02_create_directories.py

# Dependencies
import os
from pathlib import Path

def create_directories(description):
    subfolder_name:str = ''
    strDirectoryNum:str = ''

    for intCounter in range(1, 15):
        if intCounter < 10:
            strDirectoryNum = '0' + str(intCounter) 
        else:
            strDirectoryNum = str(intCounter)

        subfolder_name = strDirectoryNum + description + '_' + str(intCounter)
        if not os.path.exists(subfolder_name):
            os.makedirs(subfolder_name)

if __name__ == "__main__":
    p = 'C:\\Users\\...\\'
    os.chdir(p) # Change current directory
    Path.cwd()  # Show the current directory path
    description:str = '_Chapter'
    create_directories(description)
