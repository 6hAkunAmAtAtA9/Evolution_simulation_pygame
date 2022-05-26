from environemt import Enviroment

food = Enviroment()
print(food.x)

a = [food]
a[0].x = 2
print(food.x)

a = [0, 1]
try:
    a[2] = 3
    print(a[2])
except IndexError:
    a[1] = 3
    print(a[1])
