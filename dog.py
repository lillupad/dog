#usr/bin/python3

import sys
import os

def check_args():
    if len(sys.argv) >= 2:
        return True
    else:
        return False
    
def do_repl():
    cat_in = input()
    return cat_in

def open_file(cat_file):
    try:
        opened_file = open(os.path.join(os.getcwd(), cat_file), 'r').read()
        print(opened_file)
    except FileNotFoundError:
        print('dog: %s: No such file or directory' % sys.argv[1])
    except IsADirectoryError:
        print('dog: %s: Is a directory' % sys.argv[1])

def main():
    if check_args() == False:
        while True:
            print(do_repl())
    else:
        open_file(sys.argv[1])
        

main()