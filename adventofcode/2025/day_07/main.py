class Beam:
    def __init__(self, pos: int):
        self.pos = pos
        self.children: "list[Beam]" = []
        self.npaths = 0

    def add_child(self, child: "Beam"):
        self.children.append(child)
        child.npaths += self.npaths

class ActiveBeams:
    def __init__(self, orig: str):
        source = Beam(orig.index('S'))
        source.npaths = 1
        self._data: "dict[int, Beam]" = {source.pos: source}

    def has(self, pos: int) -> bool:
        return pos in self._data

    def pop(self, pos: int) -> Beam:
        return self._data.pop(pos)

    def get(self, pos: int) -> Beam:
        if pos not in self._data.keys():
            self._data[pos] = Beam(pos)
        return self._data[pos]

    def leaves(self) -> "list[Beam]":
        return [b for b in self._data.values() if not b.children]


with open("input.txt", 'r') as file:
    data = file.read().strip().split()

orig,traj = data[0], data[1:]

count_split = 0
beams = ActiveBeams(orig)
for step in traj:
    for pos_split in (i for i,v in enumerate(step) if v == '^'):
        if not beams.has(pos_split): continue

        count_split += 1
        pos_left  = max(0, pos_split - 1             )
        pos_right = min(   pos_split + 1, len(step)-1)

        beam_parent = beams.pop(pos_split)
        beam_parent.add_child(beams.get(pos_left ))
        beam_parent.add_child(beams.get(pos_right))


print(count_split) # PART 1: 1619
print(sum(b.npaths for b in beams.leaves())) # PART 2: 23607984027985
