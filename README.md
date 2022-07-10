# dog
a clone of the unix command `cat`, in python, in 33 lines

## installation
### prerequisites
- python 3.6 or later
### macos
1. download the .zip
2. extract the .zip
3. open a terminal window and `cd` into the directory with the `dog` executable (should be Downloads)
4. run the command `sudo cp ./dog /usr/local/bin/` to copy it to your binaries folder (you will need to enter an admin password)
5. check the program is working by running the command `dog`
### windows or linux
1. download the source code in either .zip or .tar.gz format
2. extract the source code
3. open a terminal window
4. run the command `pip install pyinstaller`. if this fails, run `python3 -m pip install pyinstaller`. if this fails, [install python](https://www.python.org/downloads/) and (windows only) add it to your PATH
5. `cd` into the folder containing the source code
6. run the command `pyinstaller -F dog.py`
7. open the `dist` folder generated, and (windows) add the executable generated to PATH or (linux) run `sudo cp ./dog /usr/local/bin/`

## usage
use the command `dog [file]`, where [file] is the file you want to read out
- if [file] does not exist, `dog` will raise a FileNotFoundError
- if [file] is a folder, `dog` will raise an IsDirectoryError
- if [file] is left blank, a repl-style interpreter will start. to close this, press `ctrl+c`

# notes
- `dog` is noticeably slower than `cat`, probably due to the fact that i'm using python
- `dog` is also technically both a [Text](https://esolangs.org/wiki/Text) interpreter and repl
- a minified version of `dog` is available in `dog_min.py` (duh). it isn't noticeably faster, but it does cut the file size down from 663 bytes to 340 bytes (what a useful optimisation)
- currently, only mac binaries are available for `dog`. i'm not sorry.
- if you want windows or linux binaries, make them yourself with `pyinstaller -F dog.py`, and if you're feeling nice, send them to me so i can make them official
