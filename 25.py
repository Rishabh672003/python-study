fromages = ['cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
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
print(fromages[1:2])
