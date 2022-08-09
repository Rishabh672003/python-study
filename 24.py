count = 0
total = 0
a = input('Enter a file name: ')

try:
    if a == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    b = open(a)
except FileNotFoundError:
    print('file not found:', a)
    exit()

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
