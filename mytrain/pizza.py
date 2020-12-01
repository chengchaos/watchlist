# -*- coding:utf-8 -*-
# 给形参指定默认值的时候，等号两边不要由空格
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppins:")
    for topping in toppings:
        print("- " + topping)
