# a = 'banana'
# if 'a' in a:
#     print('true')

# a = 'banana'
# # print(type(a))
# # print(dir(a))
# print(a.capitalize())
# print(a.upper())
# print(a.find('na',3))

# a = 42
# print(type(a))
# b = print('%d' % a)
# print(type(b))

str = 'X-DSPAM-Confidence:0.8475'
a = str.find(':')
b = str[19:]
c = float(b)
print(a)
print(b)
print(c)
d = str.find('0.8475')
print(type(d))
