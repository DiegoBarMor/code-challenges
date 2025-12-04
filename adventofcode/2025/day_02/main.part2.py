import json

with open("cache_divisors.json", 'r') as file:
    CACHE_DIVISORS = json.loads(file.read())

with open("input.txt", 'r') as file:
    ranges = [r.split('-') for r in file.read().strip().split(',')]

def yield_relevant_splits(val: int):
    s = str(val)
    for n in CACHE_DIVISORS[len(s)]:
        yield [s[i:i+n] for i in range(0, len(s), n)]

invalid_ids = set()
for v0,v1 in ranges:
    for val in range(int(v0),int(v1)+1):
        if len(str(val)) == 1: continue

        for splits in yield_relevant_splits(val):
            unique = len(set(splits)) == 1
            if unique:
                invalid_ids.add(val)
                continue

print(sum(invalid_ids))


# 69553832684 correct
