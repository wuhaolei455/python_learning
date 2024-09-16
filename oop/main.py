class Animal:
    # 类属性
    kingdom = "nanle"

    def __init__(self, name, age):
        # 私有实例属性
        self.__name = name
        self.__age = age

    # 实例方法
    def description(self):
        return f"{self.__name} is {self.__age} years old"

    # 类方法, has access to class attributes
    @classmethod
    def toString(cls):
        return f"This is {cls.__name__}"

    # 静态方法, no argument for class or instance
    @staticmethod
    def is_animal():
        return True

    # 属性访问控制
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
    
    def speak(self):
        pass

# 继承
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# dependency injection
def animal_sound(animal: Animal):
    print(animal.speak())

# 创建实例
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# 访问类方法和类属性
print(cat.toString())
print(Dog.toString())
print(f"Kingdom: {Dog.kingdom}")

# 访问实例方法和属性
print(dog.description())
print(cat.description())

# 修改属性
dog.name = "Max"
dog.age = 4
print(dog.description())

# 多态
animal_sound(dog)
animal_sound(cat)

# 静态方法
print(f"Is dog an animal? {Dog.is_animal()}")