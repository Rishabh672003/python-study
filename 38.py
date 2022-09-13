def hello(name: str) -> None:
    print('hello ' + name)


hello('lsp')
hello('rishabh')

print(5 + True)
print(6.2 // 2)
print(
    """hello
world"""
)
print('rishabh')


def the(a: str) -> None:
    print('from' + a)


a = [1, 2, 5, 4]
print((a)[0])
print(id(a))
b = sorted(a)
print(b)

c = 4
if c >= 3:
    print('lol')
else:
    print('hello from the other side')
a = 'hello'


def lol(x: str) -> None:
    print(x[1::1])


lol('hello')

x = int(input('enter a number'))
if x >= 3:
    print('hello')

alpha = 'lua is a better language fot embeding in system because it was made for it'
print(alpha)

