with open("input.txt", 'r') as file:
    ranges = [r.split('-') for r in file.read().strip().split(',')]

max_length = 0
for v0,v1 in ranges:
    max_length = max(max_length, len(v0), len(v1))

print(max_length)
