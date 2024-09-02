# 提取子列表(list)或子字符串(string)
def example1():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    text = 'Hello, World!'
    sub_list = numbers[2:5]
    sub_text = text[7:12]
    print(sub_list)  # 输出: [2, 3, 4]
    print(sub_text)  # 输出: "World"

# 整个数组
def example2():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub_list1 = numbers[:]
    sub_list2 = numbers[1:]
    sub_list3 = numbers[:-1]
    print(sub_list1)    # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sub_list2)    # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sub_list3)    # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 间隔遍历整个数组
def example3():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub_list_step = numbers[::2]
    print(sub_list_step)  # 输出: [0, 2, 4, 6, 8]

# 反转序列
def example4():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    text = "Hello, World!"
    reversed_list = numbers[::-1]
    reversed_text = text[::-1]
    print(reversed_list)  # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(reversed_text)  # 输出: "!dlroW ,olleH"
    print(numbers)        # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(text)           # 输出: "Hello, World!"

def main():
    examples = {
        1: example1,
        2: example2,
        3: example3,
        4: example4,
    }
    
    try:
        choice = int(input("Enter a number (1 to 4) to choose an example: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    example = examples.get(choice, lambda: print("Invalid choice"))
    example()

if __name__ == '__main__':
    main()