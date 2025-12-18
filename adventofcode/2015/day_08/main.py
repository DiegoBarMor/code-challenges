from collections import Counter

def len_parsed(chars: str):
    return len(eval(chars))

def count_escapables(chars: str):
    c = Counter(chars)
    return c.get("\"", 0) + c.get("\\", 0) + 2 # accoount for re-adding "" delimiters

with open("input.txt", 'r') as file:
    data = file.read().strip().split()

nchars_str = sum(map(len, data))
nchars_mem = sum(map(len_parsed, data))
nchars_esc = sum(map(count_escapables, data))

print(nchars_str - nchars_mem) # PART 1: 1371
print(nchars_esc) # PART 2: 2117
