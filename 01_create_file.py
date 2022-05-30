#!/usr/bin/env python3

# Python 3.9.5

# 01_create_file.py

# Dependency
import os

p = 'C:\\...'
os.chdir(p)

def create_file():
    new_file = open('new_file.txt', 'w')
    new_file.close()

if __name__ == "__main__":
    p = 'C:\\...'
    os.chdir(p)
    create_file()
