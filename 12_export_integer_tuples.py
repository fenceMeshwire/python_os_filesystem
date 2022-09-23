#!/usr/bin/env python3

# Python 3.9.5

# 12_export_integer_tuples.py

# Dependency 
import os

path = 'C:\\Users\\user\\...'
os.chdir(path)

tpl = [(1, 2, 3, 4, 6), (1, 2, 3, 4, 5), (3, 4, 5, 9, 1)]

with open('output.txt', 'wt', encoding='utf-8') as fout:
    for element in tpl:
        # Convert tuple to a list and join the elements of each tuple to one string:
        key = ''.join([str(x) for x in list(element)])
        fout.write(key + "\n")
        
fout.close()
