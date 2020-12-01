# -*- coding:utf-8 -*-


def decorate(func):
    print("in decorate function, decorating", func.__name__)

    def wrapper_func(*args):
        print("Executing", func.__name__)
        v = func(*args)
        return "<h1>" + v + "</h1>"
    return wrapper_func


@decorate
def myfunc(name):
    return "Hello " + name


if __name__ == "__main__":
    x = myfunc("chengchao")
    print("x = " + x)
