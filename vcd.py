import pathlib
import colorama
import sys

def danger(msg: str):
    print(colorama.Fore.RED + msg + colorama.Style.RESET_ALL)

def print_dir(dir):
    print(colorama.Fore.BLUE + dir + colorama.Style.RESET_ALL)

def print_file(file):
    print(colorama.Fore.LIGHTWHITE_EX + file + colorama.Style.RESET_ALL)

def _prepare_dir(walk_path):
    files = []
    dirs = []
    for p in walk_path.iterdir():
        if p.is_dir():
            # if 'lib' != p.name:
            dirs.append(p.name)
        else:
            files.append(p.name)
    return dirs, files

def dirtree(walk_path: pathlib.Path, depth: int = 0):
    prefix = '  ' * depth

    dirs, files = _prepare_dir(walk_path)
 
    print_dir(prefix + walk_path.name + '/')

    for d in dirs:
        dirtree(pathlib.Path(walk_path.joinpath(d)), depth + 1)

    for f in files:
        print_file(prefix + f)


def main(path: str):
    p = pathlib.Path(path)
    if not p.exists():
        danger("Path does not exist")
        return

    if not p.is_dir():
        danger("Path is not a directory")
        return

    dirtree(p)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        main(path)
    except IndexError:
        danger('Please provide path to the directory')
