# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)


def word(x, y):
    count = 0
    for letter in x:
        if letter == y:
            count = count + 1
    print(count) 


a = 'banana'
word(a, 'a')
