# -*- coding:utf-8 -*-

"""mymath - our example math module"""
pi = 2.14159


def area(r):
    """area(r): return the area of a circle with radius r."""
    global pi
    return pi * r * r
