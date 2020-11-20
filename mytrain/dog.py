class Dog():
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
