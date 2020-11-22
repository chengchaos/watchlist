# -*- coding:utf-8 -*-
# import 行让 Python 打开 pizza.py 文件，
# 并将其中的所有函数都复制到这个程序种。
# 使用 模块名.函数名调用：
# pizza.make_pizza(12, "mushrooms")
# 还可以用 ：
# from module_name import function_name
# from module_name inport *
# 导入特定的函数。
# 通过逗号分隔函数名
# 调用时直接调用
# make_pizza(16, "popperoni")
# import pizza
# import pizza as p
from pizza import make_pizza as mp

mp(16, "popperoni")
mp(12, "mushrooms", "GREEN PEPPERS", "EXTRA CHEESE")

print("end")
