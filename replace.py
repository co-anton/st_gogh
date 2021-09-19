#!/usr/bin/python3

def main(path_search: str, path_replace: str, path_file: str) -> None:
    with open(path_file, 'r') as f: file = f.read()
    with open(path_search, 'r') as f: search = f.read()
    with open(path_replace, 'r') as f: replace = f.read()
    new_file = file.replace(search, replace)
    with open(path_file, 'w') as f: f.write(new_file)

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 4
    path_search = sys.argv[1]
    path_replace = sys.argv[2]
    path_file = sys.argv[3]
    main(path_search, path_replace, path_file)
