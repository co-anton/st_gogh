#!/usr/bin/python3

import os
import sys

def safe_read(path:str) -> str:
    try:
        with open(path, 'r') as f: return f.read()
    except PermissionError:
        sys.exit(f'{path} raises a permission error')

def main(path_search: str, path_replace: str, path_file: str) -> None:
    # Searches content of file path_search in file path_file and 
    # replaces it with content of path_replace
    file = safe_read(path_file)
    search = safe_read(path_search)
    replace = safe_read(path_replace)
    new_file = file.replace(search, replace)
    assert os.access(path_file, os.W_OK), f"Cannot write {path_file}"
    with open(path_file, 'w') as f: f.write(new_file)

if __name__ == '__main__':
    assert len(sys.argv) == 4
    path_search = sys.argv[1]
    path_replace = sys.argv[2]
    path_file = sys.argv[3]
    main(path_search, path_replace, path_file)
