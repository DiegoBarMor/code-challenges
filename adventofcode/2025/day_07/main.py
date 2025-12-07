
with open("input.txt", 'r') as file:
    data = file.read().strip().split()

# data = [row for row in data if ('S' in row or '^' in row)]

class Beam:
    def __init__(self, pos: int, depth: int):
        self.pos = pos
        self.depth = depth
        self.children: "list[Beam]" = []
        self.npaths = 0

    def add_child(self, child: "Beam"):
        self.children.append(child)
        child.npaths += self.npaths


orig,traj = data[0], data[1:]


source = Beam(orig.index('S'), 0)
source.npaths = 1

count_split = 0
beams = {source.pos: source}
for depth,step in enumerate(traj, start = 1):
    splitters = (i for i,v in enumerate(step) if v == '^')

    items = list(beams.items())

    for pos_split in splitters:
        if pos_split not in beams.keys(): continue

        beam_parent = beams.pop(pos_split)
        pos_left   = max(0, pos_split - 1             )
        pos_right  = min(   pos_split + 1, len(step)-1)

        if pos_left in beams.keys():
            beam_left = beams[pos_left]
        else:
            beam_left = Beam(pos_left,  depth)
            beams[pos_left] = beam_left

        if pos_right in beams.keys():
            beam_right = beams[pos_right]
        else:
            beam_right = Beam(pos_right, depth)
            beams[pos_right] = beam_right

        beam_parent.add_child(beam_left )
        beam_parent.add_child(beam_right)

        beams[beam_left.pos ] = beam_left
        beams[beam_right.pos] = beam_right

        count_split += 1

        ###### PROPAGATE NON-SPLITTED BEAMS
        # new_beams = {}
        # for k,beam in beams.items():
        #     if beam.depth == depth:
        #         new_beams[k] = beam
        #         continue
        #
        #     child_beam = Beam(beam.pos, depth)
        #     beam.add_child(child_beam)
        #     new_beams[k] = child_beam
        #
        # beams = new_beams


print(count_split) # PART 1: 1619
print(sum(b.npaths for b in beams.values())) # PART 2: 23607984027985
