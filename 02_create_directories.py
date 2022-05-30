#!/usr/bin/env python3

# Python 3.9.5

# 02_create_directories.py

# Dependencies
import os
from pathlib import Path

def create_directories():
    subfolder_name:str = ''
    subfolder:str = '_Description'
    strDirectoryNum:str = ''

    for intCounter in range(1, 15):
        if intCounter < 10:
            strDirectoryNum = '0' + str(intCounter)
        else:
            strDirectoryNum = str(intCounter)

        subfolder_name = strDirectoryNum + subfolder
        os.makedirs(subfolder_name)

if __name__ == "__main__":
    p = 'C:\\...'
    os.chdir(p) # Change current directory
    Path.cwd()  # Show the current directory path
    create_directories()
