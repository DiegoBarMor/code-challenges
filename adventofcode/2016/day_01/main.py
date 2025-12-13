NORTH = 0
WEST  = 1
EAST  = 2
SOUTH = 3

def parse(chars: str, facing: int):
    val = int(chars[1:])
    go_right = chars[0] == 'R'
    match facing:
        case 0: # NORTH
            return (WEST, (val,0)) if go_right else (EAST, (-val, 0))
        case 1: # EAST
            return (SOUTH, (0, -val)) if go_right else (NORTH, (0, val))
        case 2: # WEST
            return (NORTH, (0, val)) if go_right else (SOUTH, (0, -val))
        case 3: # SOUTH
            return (EAST, (-val, 0)) if go_right else (WEST, (val,0))

def vec_sum(v0: tuple[int, int], v1: tuple[int, int]) -> tuple[int, int]:
    return (v0[0]+v1[0], v0[1]+v1[1])

def dL1_to_origin(v: tuple[int, int]) -> int:
    return abs(v[0]) + abs(v[1])

def get_intersection(lineA, lineB) -> bool:
    ax0, ax1, ay0, ay1 = lineA
    bx0, bx1, by0, by1 = lineB

    if ay0 == ay1: # line A is horizontal
        ax0, ax1 = sorted((ax0, ax1))
        by0, by1 = sorted((by0, by1))
        if (ax0 < bx0 < ax1) and (by0 <= ay0 <= by1):
            return (bx0,ay0)

    else: # line A is vertical
        ay0, ay1 = sorted((ay0, ay1))
        bx0, bx1 = sorted((bx0, bx1))
        if (ay0 < by0 < ay1) and (bx0 <= ax0 <= bx1):
            return (ax0,by0)


with open("input.txt", 'r') as file:
    data = file.read().strip().split(", ")


pos = (0,0)
facing = NORTH
first_duplicate_pos = None
lines = []

for s in data:
    facing, delta = parse(s, facing)
    new_pos = vec_sum(pos, delta)

    if first_duplicate_pos is not None:
        pos = new_pos; continue

    new_line = pos[0], new_pos[0], pos[1], new_pos[1]

    for line in lines:
        intersection = get_intersection(line, new_line)
        if intersection is None: continue
        first_duplicate_pos = intersection
        break

    lines.append(new_line)
    pos = new_pos


print(dL1_to_origin(pos)) # PART 1: 236
print(dL1_to_origin(first_duplicate_pos)) # PART 2: 182
