from string import ascii_lowercase
from collections import defaultdict

FORBIDDEN = "iol"
REPLACEMENT = "jpm"
NUM2CHAR = [c for c in ascii_lowercase]
CHAR2NUM  = {c:i for i,c in enumerate(NUM2CHAR)}
NCHARS = len(NUM2CHAR)

def cycle(lst: list[int]):
    carry = 0
    end = len(lst) - 1
    for i in range(end, -1, -1):
        add = int(i == end)
        newval = lst[i] + add + carry
        carry  = newval // NCHARS
        newval %= NCHARS
        if NUM2CHAR[newval] in FORBIDDEN: newval += 1
        lst[i] = newval

def has_three_consecutives(lst: list[int]):
    for i in range(len(lst)-3):
        chunk = lst[i:i+3]
        if (chunk[0]+1 == chunk[1]) and (chunk[1]+1 == chunk[2]):
            return True
    return False

def has_two_doubles(lst: list[int]):
    l0 = lst[:-1]; l1 = lst[1:]
    doubles = defaultdict(int)
    for x,y in zip(l0, l1):
        if x != y: continue
        doubles[x] += 1
    return tuple(doubles.values()) == (1,1)

def is_valid(lst: list[int]):
    return has_three_consecutives(lst) and has_two_doubles(lst[-5:])


with open("input.txt", 'r') as file:
    data = file.read().strip()


for f,r in zip(FORBIDDEN, REPLACEMENT):
    pos = data.find(f)
    if pos == -1: continue
    data = data[:pos] + r + (len(data)-1-pos)*'a'

pwd = [CHAR2NUM[c] for c in data]
while not is_valid(pwd): cycle(pwd)
first_cycle  = ''.join(NUM2CHAR[n] for n in pwd)

cycle(pwd)
while not is_valid(pwd): cycle(pwd)
second_cycle = ''.join(NUM2CHAR[n] for n in pwd)

print(first_cycle)  # PART 1: vzbxxyzz
print(second_cycle) # PART 2: vzcaabcc
