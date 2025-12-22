from collections import Counter

def correct(chars: str, func: callable) -> str:
    return func(Counter(chars).items(), key = lambda t: t[1])[0]

with open("input.txt", 'r') as file:
    data = file.read().strip().split()

corrected_v0 = ''.join(correct(col, max) for col in zip(*data))
corrected_v1 = ''.join(correct(col, min) for col in zip(*data))

print(corrected_v0) # PART 1: xdkzukcf
print(corrected_v1) # PART 2: cevsgyvd
