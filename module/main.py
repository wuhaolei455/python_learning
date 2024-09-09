from sys import *
import example.packages.no_main as no_main


if __name__ == '__main__':
    print("This is the main module.")
else:
    print("This is not the main module.")

print(version)
print(path)
print(no_main.vip_lv_name(1))