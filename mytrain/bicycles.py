# -*- coding:utf-8 -*-
bicycles = ['trek', 'cannondale', 'redline', 'specialized' ]
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
print("My first bicycle was a "+ bicycles[0].title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
motorcycles[0] = 'honda'
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a "+ first_owned.title() + ".")
print(motorcycles)
ducati = 'ducati'
motorcycles.insert(0, ducati)

motorcycles.remove('ducati')
print("ducati => "+ ducati.title() )

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
sorted(cars)
print(cars.reverse())
print(cars)
cars.sort(reverse=True)
print(cars)

print("car len => "+ str(len(cars)))