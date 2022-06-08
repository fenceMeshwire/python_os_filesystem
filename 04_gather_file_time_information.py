#!/usr/bin/env python3

# Python 3.9.7

# 04_gather_file_time_information.py

# Dependencies
import os, time

abs_filepath = 'C:\\Windows\\system32\\calc.exe'

creation_ts = os.path.getctime(abs_filepath)
last_modification_ts = os.path.getmtime(abs_filepath)
last_access_ts = os.path.getatime(abs_filepath)

creation = time.localtime(creation_ts)
modification = time.localtime(last_modification_ts)
access = time.localtime(last_access_ts)

# Accessing attributes to obtain single elements:
creation.tm_year
creation.tm_mon
creation.tm_mday
creation.tm_wday
creation.tm_hour
creation.tm_min
creation.tm_sec
