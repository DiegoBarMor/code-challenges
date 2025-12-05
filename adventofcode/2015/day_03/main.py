def map_delta(c: str) -> tuple[int, int]:
    match c:
        case '<': return (-1, 0)
        case '>': return ( 1, 0)
        case '^': return ( 0,-1)
        case 'v': return ( 0, 1)
        case _: raise ValueError(f"Unknown char: {c}")

def n_visited_first_year(deltas: str):
    pos = (0,0)
    visited = {pos}
    for c in deltas:
        dx, dy = map_delta(c)
        pos = (pos[0]+dx, pos[1]+dy)
        visited.add(pos)
    return len(visited)

def n_visited_next_year(deltas: str):
    pos_0 = (0,0)
    pos_1 = (0,0)
    visited = {pos_0}
    for i,c in enumerate(deltas):
        dx, dy = map_delta(c)
        if i % 2:
            pos_0 = (pos_0[0]+dx, pos_0[1]+dy)
            visited.add(pos_0)
        else:
            pos_1 = (pos_1[0]+dx, pos_1[1]+dy)
            visited.add(pos_1)
    return len(visited)


with open("input.txt", 'r') as file:
    data = file.read().strip()


print(n_visited_first_year(data)) # PART 1: 2592
print(n_visited_next_year (data)) # PART 2: 2360
