def testMultiReturnVal(): # tuple
    return 1, 3.14, "Hello, World!"

def testMultiReturnVal2():
    return 1, 3.14, "Hello, World!", 4, 5, 6

if __name__ == '__main__':
    a, b, c = testMultiReturnVal() # 
    print(f'a: {a}, 类型: {type(a)}')
    print(f'b: {b}, 类型: {type(b)}')
    print(f'c: {c}, 类型: {type(c)}')
