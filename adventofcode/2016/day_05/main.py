import hashlib

with open("input.txt", 'r') as file:
    door_id = file.read().strip()

idx = 0
pwd0 = ""
pwd1_cache = {str(i): None for i in range(8)}
while None in pwd1_cache.values():
    while True:
        idx += 1
        candidate = hashlib.md5(f"{door_id}{idx}".encode()).hexdigest()
        if candidate.startswith(5*'0'): break

    pos = candidate[5]
    if len(pwd0) < 8: pwd0 += pos

    if pos not in pwd1_cache.keys(): continue
    if pwd1_cache[pos] is not None: continue

    pwd1_cache[pos] = candidate[6]

pwd1 = ''.join(pwd1_cache[str(i)] for i in range(8))


print(pwd0) # PART 1: 4543c154
print(pwd1) # PART 2: 1050cbbd
