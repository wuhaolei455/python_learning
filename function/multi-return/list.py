def testMultiReturnValList(): # List
    return [1, 3.14, "Hello, World!"]

if __name__ == '__main__':
    result = testMultiReturnValList()
    print(f'结果: {result}, 类型: {type(result)}')
    print(f'第一个元素: {result[0]}, 类型: {type(result[0])}')
    print(f'第二个元素: {result[1]}, 类型: {type(result[1])}')
    print(f'第三个元素: {result[2]}, 类型: {type(result[2])}')

