import hashlib

with open("input.txt", 'r') as file:
    key = file.read().strip()

ans_5 = 0
candidate = ""
while not candidate.startswith(5*'0'):
    ans_5 += 1
    candidate = hashlib.md5(f"{key}{ans_5}".encode()).hexdigest()

ans_6 = ans_5
while not candidate.startswith(6*'0'):
    ans_6 += 1
    candidate = hashlib.md5(f"{key}{ans_6}".encode()).hexdigest()

print(ans_5) # PART 1: 346386
print(ans_6) # PART 2: 9958218
