"""
The 'cat' Program Implemented in Python 3

The Unix 'cat' utility reads the contents
of file(s) specified through stdin and 'conCATenates'
into stdout. If it is run without any filename(s) given,
then the program reads from standard input itself,
which means it simply copies stdin to stdout.

It is fairly easy to implement such a program
in Python, and as a result countless examples
exist online. This particular implementation
focuses on the basic functionality of the cat
utility. Compatible with Python 3.6 or higher.

Syntax:
python3 cat.py [filename1] [filename2] etc...
Separate filenames with spaces.

wuhaolei - 09/02/2024
"""
import sys

def with_files(files):
    try:
        contents = [open(file).read() for file in files]
    except OSError as err:
        exit(print(f"cat: error reading files ({err})"))

    for content in contents:
        sys.stdout.write(content)

def no_files():
    try:
        while True:
            print(input())
    except EOFError | KeyboardInterrupt:
        exit()

def main():
    if not sys.argv[1:]:
        no_files()
    else:
        with_files(sys.argv[1:])

if __name__ == '__main__':
    main()