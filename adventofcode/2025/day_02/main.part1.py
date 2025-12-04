import json

with open("cache_divisors.json", 'r') as file:
    CACHE_DIVISORS = json.loads(file.read())

with open("input.txt", 'r') as file:
    ranges = [r.split('-') for r in file.read().strip().split(',')]

def yield_relevant_splits(val: int):
    s = str(val)
    for n in CACHE_DIVISORS[len(s)]:
        yield (s[i:i+n] for i in range(0, len(s), n))

invalid_ids = []
for v0,v1 in ranges:
    for ival in range(int(v0),int(v1)+1):
        sval = str(ival)
        l = len(sval)
        if l % 2: continue

        sv0, sv1 = sval[:l//2], sval[l//2:]
        if sv0 != sv1: continue

        invalid_ids.append(ival)


print(sum(invalid_ids))

# answer first half: 53420042388
