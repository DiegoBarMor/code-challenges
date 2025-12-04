import sys
import json

SIZE_CACHE = int(sys.argv[1])
assert SIZE_CACHE > 2

cache = [{1}, {1}] + [set() for _ in range(SIZE_CACHE-2)]
for num in range(2,SIZE_CACHE):
    for divisor in range(1,num):
        if num % divisor: continue
        cache[num].add(divisor)
        cache[num].update(cache[divisor])

with open("cache_divisors.json", 'w') as file:
    file.write(json.dumps([list(s) for s in cache]))
