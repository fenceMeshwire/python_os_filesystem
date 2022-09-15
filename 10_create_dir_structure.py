#!/usr/bin/env python3

# Python 3.9.5

# 10_create_dir_structure.py

import os
from pathlib import Path

def create_dir_structure(path, main_folders, subfolders):
    os.chdir(path)
    for main_folder in main_folders:
        if not os.path.exists(main_folder):
            os.mkdir(main_folder)
        for folder in os.listdir(path):
            main_folder_path = str(Path(path, folder))
            for subfolder in subfolders:
                if not os.path.exists(str(Path(main_folder_path, subfolder))):
                    os.mkdir(str(Path(main_folder_path, subfolder)))
            main_folder_path = path

if __name__ == '__main__':
    path = 'C:\\Documents\\Level\\'
    main_folders = ['SERV01F', 'SERV02F', 'SERV03F', 'SERV04F']
    subfolders = ['Studies', 'Tasks', 'Misc']
    create_dir_structure(path, main_folders, subfolders)
