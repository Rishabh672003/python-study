# a = open('output.txt', 'w')
# print(a)
# line1 = 'this is a line, \n '
# a.write(line1)
# a.close()
#
def open_file(x):
    a = open(x)
    b = a.read()
    b = b.rstrip()
    print(b.upper())

a = input("enter file name: ")
open_file(a)

# a = open('20.py')
# b = a.read()
# c = b.find('banana')
# print(c)

