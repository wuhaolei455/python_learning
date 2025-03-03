def testMultiReturnVal(): # tuple
    return 1, 3.14, "Hello, World!"

if __name__ == '__main__':
    res = testMultiReturnVal()
    print(f'结果: {res}, 类型: {type(res)}')
    a, b, c = testMultiReturnVal() # 
    print(f'a: {a}, 类型: {type(a)}')
    print(f'b: {b}, 类型: {type(b)}')
    print(f'c: {c}, 类型: {type(c)}')