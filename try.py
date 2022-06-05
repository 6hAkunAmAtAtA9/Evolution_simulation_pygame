import random
a = [1, 2, 3, 4, 5]
a.pop(random.randint(0, len(a) - 1))
a.append(6)
print(a)