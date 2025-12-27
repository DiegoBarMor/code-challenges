def iter_permutations(*args):
    if not args:
        yield (); return

    for i,x in enumerate(args):
        for c in iter_permutations(*args[:i], *args[i+1:]):
            yield c + (x,)

with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

names =\
    set(row.split()[0] for row in data) |\
    set(row.split()[2] for row in data)

distances = {name:{} for name in names}
for row in data:
    n0, _, n1, _, dist = row.split()
    distances[n0][n1] = int(dist)
    distances[n1][n0] = int(dist)

max_dist = 0
min_dist = float("inf")
for combo in iter_permutations(*names):
    dist = sum(distances[name0][name1] for name0,name1 in zip(combo[:-1], combo[1:]))
    min_dist = min(min_dist, dist)
    max_dist = max(max_dist, dist)


print(min_dist) # PART 1: 251
print(max_dist) # PART 2: 898
