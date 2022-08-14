fhand = open('mbox-short')

counts = dict()

for line in fhand:
    words = line.strip()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

# fhand = open('mbox-short')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print(line)
