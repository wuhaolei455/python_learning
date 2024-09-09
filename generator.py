# yield.py https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
# use yield to create a generator
# generator is an iterator
def simple_generator_example():
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    for value in simple_generator():
        print(value, end=' ')
    print()  # 输出: 1 2 3

# 使用生成器生成斐波那契数列
def fibonacci_generator_example():
    def fibonacci_generator(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    for value in fibonacci_generator(10):
        print(value, end=' ')
    print()  # 输出: 0 1 1 2 3 5 8 13 21 34

# 使用生成器生成无限序列
def infinite_sequence_example():
    def infinite_numbers():
        num = 0
        while True:
            yield num
            num += 1
    
    gen = infinite_numbers()
    for _ in range(5):
        print(next(gen), end=' ')
    print()  # 输出: 0 1 2 3 4

# 使用生成器表达式
def generator_expression_example():
    numbers = [1, 2, 3, 4, 5]
    squared = (x * x for x in numbers)
    
    for value in squared:
        print(value, end=' ')
    print()  # 输出: 1 4 9 16 25

def main():
    print("Simple generator example:")
    simple_generator_example()
    
    print("Fibonacci generator example:")
    fibonacci_generator_example()
    
    print("Infinite sequence example:")
    infinite_sequence_example()
    
    print("Generator expression example:")
    generator_expression_example()

if __name__ == '__main__':
    main()