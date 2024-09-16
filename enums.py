from enum import *

@unique
class Color(IntEnum): # Enum
    RED = 1
    GREEN = 2
    BLUE = 3

# 自定义枚举类遍历
def enum_basic_traversal():
    for name, color in Color.__members__.items(): # a dict store Singleton, @property
        print(f'name: {name}, value: {color.value}')

# 枚举类is 和 == 比较
def enum_basic_comparison():
    c1 = Color.RED
    c2 = Color.RED
    print(c1 == c2, c1 is c2)

# 枚举类运算符比较
def enum_basic_comparison2():
    try:
        print(',\n'.join(s.name for s in sorted(Color)))
    except TypeError as err:
        print(' Error : {}'.format(err))
 
def main():
    enum_basic_traversal()
    enum_basic_comparison()
    enum_basic_comparison2()
    # methods = {
    #     1: enum_basic_traversal,
    #     2: enum_basic_comparison,
    #     3: enum_basic_comparison2,
    # }
    
    # try:
    #     choice = int(input("Enter a number (1 to 3) to choose a method: "))
    # except ValueError:
    #     print("Invalid input. Please enter an integer.")
    #     return
    
    # method = methods.get(choice, lambda: print("Invalid choice"))
    # method()


if __name__ == '__main__':
    main()