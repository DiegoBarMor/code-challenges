from collections import Counter

with open("input.txt", 'r') as file:
    data = file.read().strip()

count = Counter(data)

pos = 0
for i,c in enumerate(data):
    pos += (1 if c == '(' else -1)
    if pos == -1: break

print(count['('] - count[')']) # PART 1: 232
print(i+1) # PART 2: 1783
