VOWELS = set("aeiou")
FORBIDDEN = {('a','b'), ('c','d'), ('p','q'), ('x','y')}

def at_least_3_vowels(chars: set[str]):
    # return len(chars.intersection(VOWELS)) >= 3
    return sum(c in VOWELS for c in chars) >= 3

def has_double(pairs: set[tuple[str, str]]):
    return any(map(lambda t: t[0] == t[1], pairs))

def not_forbidden(pairs: set[tuple[str, str]]):
    return not pairs.intersection(FORBIDDEN)

def is_nice(s: str) -> bool:
    if len(s) < 3: return False

    pairs = set(zip(s[:-1:2], s[1::2])) | set(zip(s[1:-1:2], s[2::2]))
    return at_least_3_vowels(s) and has_double(pairs) and not_forbidden(pairs)

with open("input.txt", 'r') as file:
    data = file.read().strip().split()


print(sum(map(is_nice, data))) # PART 1: 258
print() # PART 2:
