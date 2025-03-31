from contextlib import contextmanager

class MyOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print('MyOpen.__init__')

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('MyOpen.__enter__')
        return self.file

    # type: exception type
    # value: exception value
    def __exit__(self, type, value, traceback):
        print(f'MyOpen.__exit__')
        if (type is ValueError):
            print(f'ValueError: {value}')
        self.file.close()
        return True

@contextmanager
def my_open(filename, mode):
    print('MyOpen')
    try:
        yield open(filename, mode)
    finally:
        print('MyOpen finally')