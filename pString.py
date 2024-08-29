from string import Template

# str.format()
def method1():
    print('This program is being run by {}, {}'.format('python', 'haha'))

# f-string
def method2():
    name = "python"
    comment = "haha"
    print(f'This program is being run by {name}, {comment}')

# class Template
def method3():
    template = Template('This program is being run by $name, $comment')
    print(template.substitute(name='python', comment='haha'))

# dict
def method4():
    data = {"name": "python", "comment": "haha"}
    print(f'This program is being run by {data["name"]}, {data["comment"]}')
    print("This program is being run by {name}, {comment}".format(**data))

def method5():
    number = 123.456
    print(f"Number: {number:.2f}")

def main():
    methods = {
        1: method1,
        2: method2,
        3: method3,
        4: method4,
        5: method5,
    }
    
    try:
        choice = int(input("Enter a number (1 to 5) to choose a method: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    method = methods.get(choice, lambda: print("Invalid choice"))
    method()

if __name__ == '__main__':
    main()