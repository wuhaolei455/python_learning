from my_open import MyOpen, my_open


def main():
    with MyOpen('./with/file.txt', 'w') as file:
        file.write('Hello, ')    
        raise ValueError('ValueError')

def main2():
    with my_open('./with/file.txt', 'a') as file:
        file.write('World!')    

if __name__ == '__main__':
    main()
    main2()