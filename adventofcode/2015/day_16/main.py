import re

class Sue:
    def __init__(self, chars: str):
        m = re.fullmatch(r"^Sue (?P<idx>\d+): (?P<parts>.+)$", chars)
        self.idx = m.group("idx")
        self.parts = {}
        for part in m.group("parts").split(", "):
            k,v = part.split(": ")
            self.parts[k] = int(v)

    def matches_v0(self, ref: dict[str, int]):
        return all(ref[k] == v for k,v in self.parts.items())

    def matches_v1(self, ref: dict[str, int]):
        for k,v in self.parts.items():
            r = ref[k]
            if k in ("cats", "trees"):
                if r < v: continue
                return False
            if k in ("pomeranians", "goldfish"):
                if r > v: continue
                return False
            if v != r: return False
        return True


REF = {
    "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
    "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1,
}

with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

sues = [Sue(row) for row in data]

candidates = list(filter(lambda s: s.matches_v0(REF), sues))
assert len(candidates) == 1
aunt_0 = candidates[0]

candidates = list(filter(lambda s: s.matches_v1(REF), sues))
assert len(candidates) == 1
aunt_1 = candidates[0]

print(aunt_0.idx) # PART 1: 40
print(aunt_1.idx) # PART 2: 241
