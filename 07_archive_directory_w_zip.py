#!/usr/bin/env python3

# Python 3.9.5

# 07_archive_directory.py

# Purpose: Back up a directory with all subdirectories and files.

# Dependencies
from datetime import datetime
import os
import zipfile

def zip_directory(directory, time_stamp):
    
    directory = os.path.abspath(directory)
    # A: Check if a zip file already exists and if so add 1 to the consecutive number
    while True:
        zip_file_name = os.path.basename(directory) + "_" + time_stamp + ".zip"
        if not os.path.exists(zip_file_name):
            break

    # B: Make a ZIP file. The 'write' method is used to attach further directories to the ZIP file.
    print(f'Creating new archive: {zip_file_name}')
    back_up = zipfile.ZipFile(zip_file_name, 'w')
    
    # C: Use walk and add files to the current ZIP file:
    for dir_name, sub_dir, filenames in os.walk(directory):
        print(f'Writing files to: {dir_name}')
        # Write current directory to ZIP file:
        back_up.write(dir_name)
        # Write all files from this directory to the ZIP file:
        for filename in filenames:
            basename = os.path.basename(directory) + '_'
            if filename.startswith(basename) and filename.endswith('.zip'):
                continue # Don't write existing ZIP files to the backup. 
            back_up.write(os.path.join(dir_name, filename))
    back_up.close()
    print('Archiving completed.')

def create_time_stamp():
    # Create local time (lt)
    lt = datetime.now()
    year, month, day, hour, minute = lt.year, lt.month, lt.day, lt.hour, lt.minute
    if int(month) < 10: month = "0" + str(month)
    if int(day) < 10: day = "0" + str(day)
    if int(hour) < 10: month = "0" + str(hour)
    if int(minute) < 10: day = "0" + str(minute)
    time_stamp = str(year) + str(month) + str(day) + "_" + str(hour) + str(minute)
    return time_stamp


if __name__ == '__main__':
    directory = 'C:\\temp\\test'
    os.chdir(directory)
    time_stamp = create_time_stamp()
    zip_directory(directory, time_stamp)
