def _f(): pass
FunctionType = type(_f)
LambdaType = type(lambda: None)         # Same as FunctionType
CodeType = type(_f.__code__)
MappingProxyType = type(type.__dict__)

def printHello(self, name='Py'):
    print('Hello,', name)

Hello = type('Hello', (object,), dict(hello = printHello))

h = Hello()
h.hello()
print(type(Hello)) # 元类, <class 'type'>
print(type(h)) # Hello