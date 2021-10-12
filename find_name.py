#!/usr/bin/python3 

def main(name: str, path_config: str) -> int:
    # Returns the name index if name is found
    # otherwise returns -1
    with open(path_config, 'r') as f:
        lines = f.readlines()
    i = 1
    for line in lines:
        if not line.startswith('    {"name"'): continue
        if name in line: return i
        i += 1
    return -1  

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 3
    name_search = sys.argv[1]
    path_config = sys.argv[2]
    print(main(name_search, path_config))
