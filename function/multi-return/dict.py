def testMultiReturnValDict():
    return {'int_val': 1, 'float_val': 3.14, 'str_val': "Hello, World!"}

if __name__ == '__main__':
    result = testMultiReturnValDict()
    print(f'结果: {result}, 类型: {type(result)}')
    print(f'整数值: {result["int_val"]}, 类型: {type(result["int_val"])}')
    print(f'浮点数值: {result["float_val"]}, 类型: {type(result["float_val"])}')
    print(f'字符串值: {result["str_val"]}, 类型: {type(result["str_val"])}')
