# -*- coding:utf-8 -*-
import fileinput


def main():
    for line in fileinput.input():
        if not line.startswith("##"):
            print(line, end="")


if __name__ == '__main__':
    """如果被当作脚本调用，运行时的当前模块名称将会是 __main__"""
    main()
else:
    print("")
    # 本模块的初始化代码
