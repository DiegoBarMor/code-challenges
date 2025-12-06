VOWELS = set("aeiou")
FORBIDDEN = {('a','b'), ('c','d'), ('p','q'), ('x','y')}

def get_pairs(chars: str):
    return (
        set(zip(chars[ :-1:2], chars[1::2])),
        set(zip(chars[1:-1:2], chars[2::2]))
    )

def at_least_3_vowels(chars: str):
    return sum(c in VOWELS for c in chars) >= 3

def has_repeated(pairs: set[tuple[str, str]]):
    return any(map(lambda t: t[0] == t[1], pairs))

def not_forbidden(pairs: set[tuple[str, str]]):
    return not pairs.intersection(FORBIDDEN)

def has_double_pairs(chars: str):
    for i in range(len(chars)-2):
        pair_i = (chars[i], chars[i+1])
        for j in range(i+2, len(chars)-1):
            pair_j = (chars[j], chars[j+1])
            if pair_i == pair_j:
                return True
    return False

def has_repeated_with_inbetween(chars: str):
    p0_a,p1_a = get_pairs(chars[ ::2])
    p0_b,p1_b = get_pairs(chars[1::2])
    return has_repeated(p0_a|p1_a) or has_repeated(p0_b|p1_b)


def is_nice_v1(s: str) -> bool:
    if len(s) < 3: return False
    p0,p1 = get_pairs(s)
    return at_least_3_vowels(s) and has_repeated(p0|p1) and not_forbidden(p0|p1)

def is_nice_v2(s: str) -> bool:
    if len(s) < 4: return False
    return has_repeated_with_inbetween(s) and (has_double_pairs(s))


with open("input.txt", 'r') as file:
    data = file.read().strip().split()


print(sum(map(is_nice_v1, data))) # PART 1: 258
print(sum(map(is_nice_v2, data))) # PART 2: 53
