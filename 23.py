# a = input("enter a filename: ")
# b = open('mbox-short.txt')
# for word in b:
#     count = 0
#     word = word.rstrip()
#     if word.find('X-DSPAM-Confidence: ') == -1:
#         continue

count = 0
total = 0
b = open('mbox-short.txt')
for line in b:
    # line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos + 1 :].strip()
        spam = float(number)
        total = total + spam
print(count)
print(total)
average = total / count
print(average)
