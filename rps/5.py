import random
x = ord('a')
y = ord('z')

a = random.randint(x, y)
b = random.randint(x, y)
c = chr(a)
d = chr(b)
print(c, ',', d)
