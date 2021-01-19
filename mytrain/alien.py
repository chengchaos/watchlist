# -*- coding:utf-8 -*-
import print as print

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(favorite_languages)

for k, v in favorite_languages.items():
    print("Key" + k + " => " + v.title())


for lan in set(favorite_languages.values()):
    print("lan => " + lan)

# 输入回车以后继续
# message = input("Tell me somehing, and I will repeat it back to you: ")
# print("The Message: => " + message)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
