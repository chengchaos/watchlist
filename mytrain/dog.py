# -*- coding:utf-8 -*-
import mytrain.mymath
import importlib
from mytrain.mymath import pi, area
import sys

importlib.reload(mytrain.mymath)


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性 name 和 age"""

        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog("willie", 6)

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()


def main():
    print(mytrain.mymath.pi)
    print(pi)
    print(area(10))
    print("sys.path => " + str(sys.path))
    print("sys..prefix => " + sys.prefix)


if __name__ == "__main__":
    main()
