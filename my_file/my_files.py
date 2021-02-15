# -*- coding:utf-8 -*-
# This file's name is my_files.py
import os
import sys


class Animal:
    age = 0

    def call(self):
        None

    def do_eat(self):
        print("age => ", self.age)
        print("Animal eat")


class Dog(Animal):

    def __init__(self, age):
        self.age = age

    def __del__(self):
        print("dog is del")

    def call(self):
        print("wang ")


def change_this():
    return


def test_os():
    os_name = os.name
    print("os_name =>", os_name)
    print("sys.platform ->", sys.platform)
    # print("environ -> ", os.environ)

    env = os.environ
    for k in env:
        None
        # print(k, " -> ", os.getenv(k))

    print("执行命令")
    # os.system("ping www.baidu.com")
    print(os.getcwd())
    os.chdir("c:/works")
    print(os.getcwd())
    os.listdir("c:\\works\\git-repo")

    abs_path = os.path.abspath(".")
    print("abs_path =>", abs_path)


if __name__ == "__main__":
    dog = Dog(20)
    dog.call()
    dog.do_eat()
