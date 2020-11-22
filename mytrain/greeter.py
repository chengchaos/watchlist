# -*- coding:utf-8 -*-
def greet_user(username):
    """显示问候语"""
    print("Hello, " + username.title() + "!")


greet_user("chengchao")


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print("musician => " + musician)


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关于一个人能的信息"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print("musician => " + str(musician))


def greet_users(names):
    """向列表种的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "."
        print(msg)


usernames = ["hannah", 'ty', 'margot']
greet_users(usernames)


def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("Making a pizza with the following toppinghs:\n")
    for topping in toppings:
        print("- " + topping)


make_pizza("popperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")
