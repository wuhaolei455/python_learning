from sys import *
import example.packages.no_main as no_main


if __name__ == '__main__':
    print("This is the main module, main")
else:
    print("This is not the main module, main")

print(version)
print(path)
print(no_main.vip_lv_name(1))