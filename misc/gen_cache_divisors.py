import sys
import json

SIZE_CACHE = int(sys.argv[1])
assert SIZE_CACHE > 2

def get_divisors(ndivisors):
    cache = [{1}, {1}] + [set() for _ in range(ndivisors-2)]
    for num in range(2,ndivisors):
        for divisor in range(1,num):
            if num % divisor: continue
            cache[num].add(divisor)
            cache[num].update(cache[divisor])
    return cache

with open("cache_divisors.json", 'w') as file:
    file.write(json.dumps([list(s) for s in get_divisors(SIZE_CACHE)]))
