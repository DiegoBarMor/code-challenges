def parse(line):
    sign = 1 if line[0] == 'R' else -1
    return sign, int(line[1:])

with open("input.txt", 'r') as file:
    rotations = [parse(line.strip()) for line in file.read().strip().split()]

pos = 50
count_landed_0 = 0
count_jumped_0 = 0

for sign,delta in rotations:
    if delta >= 100:
        count_jumped_0 += delta // 100
        delta %= 100

    start_from_0 = pos == 0
    pos += sign*delta

    if pos < 0:
        count_jumped_0 += int(not start_from_0)
        pos += 100

    elif pos > 100:
        count_jumped_0 += int(not start_from_0)
        pos -= 100

    if pos in (0, 100):
        count_landed_0 += 1
        pos = 0

print(count_landed_0) # PART 1: 1139
print(count_landed_0 + count_jumped_0) # PART 2: 6684
