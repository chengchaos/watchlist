# -*- coding:utf-8 -*-
# This file's name is demo1.py
import re


# re.search 返回 match
# re.compile 返回 pattern
# pattern.search 返回 match
# start() 返回匹配开始位置
# end() 返回结束位置
# group() 返回被匹配的字符串
# groups() 返回一个包含正则中所有小组字符串的元组。
def change_this():
    print(re.__version__)
    print(re.__all__)

    pattern = "模块"
    my_str = "学习热模块"
    match = re.search(pattern, my_str)
    print(match.start())
    print("end => ", match.end())
    print("res => ", my_str[match.start():match.end()])
    print("group =>", match.group())

    match2 = re.search("([0-9]*)([a-z]*)([0-9]*)", "123abc445++")
    print(match2.groups())
    print(match2.group(0))
    print(match2.group(1))
    print(match2.group(2))
    print(match2.group(3))

    return


def demo_compile():
    pattern = re.compile("hello")
    match = pattern.search("Hello world, you must use hello OK?")
    print(match.group())


def demo_match():
    pattern = "^cn$"
    my_str = "cnwww.baidu.com"
    res = re.match(pattern, my_str)
    print("res =>", res)

    if res is not None:
        print("group => ", res.group())
        print("groups => ", res.groups())


if __name__ == "__main__":
    print("nothing.")
    # change_this()
    demo_compile()
    print("汉字的编码范围 [\u4e00-\u9fa5]")
    demo_match()
