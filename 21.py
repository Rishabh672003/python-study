# a = open('mbox.txt')
# count = 0
# for line in a:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

a = input("Enter the file name here: ")
try:
    b = open(a)
except:
    print("Enter a valid filename")
    exit()

count = 0
for line in b:
    if line.startswith('Subject:'):
        count = count + 1

print(count)

