class Meta:
    pass

def echo(obj):
    print(obj)


def main():
    meta = Meta 
    echo(meta) # <class '__main__.Meta'>

if __name__ == '__main__':
    main()