#!/usr/bin/env python3

# Python 3.9.5

# Dependency
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_directory:
    print('Name of the temporary directory:', temp_directory)
    
# The temporary directory is deleted after this step.
