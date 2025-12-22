import re

class Marker:
    def __init__(self, re_match):
        self.i, self.j = re_match.span()
        self.subsequent, self.repeat = map(int,
            re_match.group().lstrip('(').rstrip(')').split('x')
        )

    def __len__(self): return self.j - self.i


def get_markers(chars: str):
    return (Marker(m) for m in re.finditer(r"\(\d+x\d+\)", chars))

def decompress_v1(chars: str) -> int:
    current_pos = 0
    lenexpanded = len(chars)
    for m in get_markers(chars):
        if m.i < current_pos: continue
        current_pos = m.j + m.subsequent
        lenexpanded += m.subsequent*(m.repeat-1) - len(m)
    return lenexpanded

def decompress_v2(chars: str) -> int:
    reps = [1 for _ in chars]
    for m in get_markers(chars):
        for i in range(m.j, m.j+m.subsequent):
            reps[i] *= m.repeat
        for i in range(m.i, m.j):
            reps[i] = 0
    return sum(reps)


with open("input.txt", 'r') as file:
    data = file.read().strip().replace(' ', '').replace('\n', '')


print(decompress_v1(data)) # PART 1: 183269
print(decompress_v2(data)) # PART 2: 11317278863
