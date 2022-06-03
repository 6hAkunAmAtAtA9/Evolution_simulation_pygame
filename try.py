import random
a = []
while len(a) < 10:
    a.append(random.choice(("up", 'down', 'right', 'left')))
a.append('birth')
random.shuffle(a)

print(a)
random.shuffle(a)

print(a)
