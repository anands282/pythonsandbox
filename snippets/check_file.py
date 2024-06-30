#Checking if a file exists in two ways
#1- Using the OS module
import os
exists = os.path.isfile('/path/to/file')

#2- Use the pathlib module for a better performance
from pathlib import Path
config = Path('/path/to/file')
if config.is_file():
    pass