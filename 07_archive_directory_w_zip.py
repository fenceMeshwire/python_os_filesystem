#!/usr/bin/env python3

# Python 3.9.5

# 07_archive_directory.py

# Purpose: Back up a directory with all subdirectories and files.

# Dependencies
import os
import zipfile

def zip_directory(directory):
  
    directory = os.path.abspath(directory)
    consecutive_number = 1
    # A: Check if a zip file already exists and if so add 1 to the consecutive number
    while True:
        zip_file_name = os.path.basename(directory) + "_" + str(consecutive_number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        consecutive_number += 1

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

if __name__ == '__main__':
    directory = 'C:\\temp\\test'
    os.chdir(directory)
    zip_directory(directory)
