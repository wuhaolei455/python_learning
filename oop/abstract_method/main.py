from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def say(self):
        print('I am a person')

class Student(Person):
    def say(self):
        super().say()
        print('I am a student')

if __name__ == '__main__':
    s = Student()
    s.say()
    # p.say()  # TypeError: Can't instantiate abstract class Person with abstract method say
