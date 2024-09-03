# for string, list, tuple
def iterator_basic_example():
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)
    
    try:
        while True:
            number = next(iterator)
            print(number, end=' ') # 输出: 1 2 3 4 5
    except StopIteration:
        print('over')  

# 自定义迭代器
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def custom_iterator_example():
    rev = ReverseIterator([1, 2, 3, 4, 5])
    for item in rev:
        print(item, end=' ') # 输出: 5 4 3 2 1
    print('over')  

def main():
    methods = {
        1: iterator_basic_example,
        2: custom_iterator_example,
    }
    
    try:
        choice = int(input("Enter a number (1 to 2) to choose a method: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    method = methods.get(choice, lambda: print("Invalid choice"))
    method()

if __name__ == '__main__':
    main()