#!/usr/bin/env python3

# Python 3.9.5

# 12_check_file_exists.py

# Dependency
import os

# Change the current working directory
path = 'C:\\Users\\...'
os.chdir(path)

# Prepare list result for output to a CSV file, e.g. one line:
result = ['result', 'message', 'output', '123']
str_result = ','.join(str(x) for x in result)

# Check if the file to be exported exists. 
# If not then write the file and a message, else write only a message.

if not os.path.exists('export.csv'):
    with open('export.csv', 'wt') as export_file:
        export_file.write(str_result)
    print('File written to filesystem successfully.')
else:
    print('File exists already')
