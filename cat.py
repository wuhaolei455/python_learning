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