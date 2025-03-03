# *args 是用来接收任意数量的位置参数, return tuple
# **kwargs 是用来接收任意数量的关键字参数, return dict
def main( *args, gender = 'FEMALE', **kwargs):
    print(args, gender, kwargs)

if __name__ == '__main__':
    main("HAHA", "SADSADSA", 123, gender='MALE', name='Tom', age=18)
    main("HAHA", "SADSADSA", 123, name='Tom', age=18)