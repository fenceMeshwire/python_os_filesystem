#!/usr/bin/env python3

# Python 3.9.5

# 23_export_dir_content_w_creation_date.py

# Dependencies
from datetime import datetime
import os
import pandas as pd

path = 'C:\\Users\\User\\Downloads'
os.chdir(path)

number_of_files = pd.Series([filename for filename in os.listdir('.') if os.path.isfile(filename)])
creation_of_files = pd.Series([datetime.fromtimestamp(os.path.getmtime(filename)) for filename in os.listdir('.') if os.path.isfile(filename)])
files = zip(number_of_files, creation_of_files)

files = pd.DataFrame(files)
files.columns=["filename", "creation_date"]
files['creation_date'] = pd.to_datetime(files["creation_date"]).dt.date

files[files.groupby('filename')['creation_date'].transform('max') == files['creation_date']]
result = files.sort_values(by='creation_date', ascending=False, ignore_index=True)

result.to_csv('file_content.csv', index=False, encoding='utf-8')
