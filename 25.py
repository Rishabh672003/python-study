fromages = ['cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
numbers1 = [1, 0]
empty = []
print(fromages, numbers, empty)
fromages[0] = 'Brie'
print(fromages)
a = 'cheddar' in fromages
print(a)
for cheese in fromages:
    print(cheese)
c = len(fromages)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
print(fromages[:])
d = numbers.reverse()
print(numbers)
e = numbers.extend(numbers1)
print(numbers)
f = numbers.sort()
print(numbers)
g = numbers.pop(1)
print(g)
print(numbers)
print(sum(numbers))
