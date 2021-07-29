from pathlib import Path
import re
import os

files_path = Path('/Users/natal/Documents/Cakap Intermediate Business English')

for file in files_path.iterdir():
    directory = file.parent
    extention = file.suffix

    name = file.stem
    
    folder_name = re.split(r'\.', name)[0]
    new_path = files_path.joinpath(folder_name)

    if not new_path.exists():
        new_path.mkdir()

    new_file_path = new_path.joinpath(f'{name}{extention}')
    file.replace(new_file_path)