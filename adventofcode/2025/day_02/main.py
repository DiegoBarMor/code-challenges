def get_max_length(ranges):
    max_length = 0
    for v0,v1 in ranges:
        max_length = max(max_length, len(v0), len(v1))
    return max_length

def get_divisors(ndivisors):
    cache = [{1}, {1}] + [set() for _ in range(ndivisors-2)]
    for num in range(2,ndivisors):
        for divisor in range(1,num):
            if num % divisor: continue
            cache[num].add(divisor)
            cache[num].update(cache[divisor])
    return cache

def yield_relevant_splits(val: int, divisors):
    s = str(val)
    for n in divisors[len(s)]:
        yield (s[i:i+n] for i in range(0, len(s), n))


with open("input.txt", 'r') as file:
    ranges = [r.split('-') for r in file.read().strip().split(',')]

invalid_ids_0 = []
for v0,v1 in ranges:
    for ival in range(int(v0),int(v1)+1):
        sval = str(ival)
        l = len(sval)
        if l % 2: continue

        sv0, sv1 = sval[:l//2], sval[l//2:]
        if sv0 != sv1: continue

        invalid_ids_0.append(ival)


divisors = get_divisors(get_max_length(ranges)+1)
invalid_ids_1 = set()
for v0,v1 in ranges:
    for val in range(int(v0),int(v1)+1):
        if len(str(val)) == 1: continue

        for splits in yield_relevant_splits(val, divisors):
            unique = len(set(splits)) == 1
            if unique:
                invalid_ids_1.add(val)
                continue


print(sum(invalid_ids_0)) # PART 1: 53420042388
print(sum(invalid_ids_1)) # PART 2: 69553832684
