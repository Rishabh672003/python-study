import random
a = 8
b = 4

c = random.randint(1, 4)

if c == 1:
    d = "+"
    e = a + b
elif c == 2:
    d = "-"
    e = a - b
elif c == 3:
    d = "*"
    e = a * b
else:
    d = "/"
    e = a / b

print("result is", a, d, b, "=", e)
