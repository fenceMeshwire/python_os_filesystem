#!/usr/bin/env python3

# Python 3.9.5

# 01_create_file.py

# Dependency
import os

def create_file():
    new_file = open('new_file.txt', 'w')
    new_file.close()

if __name__ == "__main__":
    p = 'C:\\...'   # Define absolute path
    os.chdir(p)     # Change working directory
    create_file()
