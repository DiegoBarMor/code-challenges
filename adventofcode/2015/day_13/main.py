def iter_permutations(*args):
    if not args:
        yield (); return

    for i,x in enumerate(args):
        for c in iter_permutations(*args[:i], *args[i+1:]):
            yield c + (x,)

def get_best_friendship(relations: dict[str, dict[str, int]]):
    best_friendship = 0
    for combo in iter_permutations(*relations.keys()):
        combo += (combo[0],) # make it circular
        friendship = 0
        for name0,name1 in zip(combo[:-1], combo[1:]):
            friendship += relations[name0][name1]
            friendship += relations[name1][name0]
        best_friendship = max(best_friendship, friendship)
    return best_friendship


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

names = set(row.split()[0] for row in data)
relationships = {name: {} for name in names}
for row in data:
    parts = row.rstrip('.').split()
    name0 = parts[0]
    name1 = parts[-1]
    sign  = 1 if parts[2] == "gain" else -1
    value = sign * int(parts[3])
    relationships[name0][name1] = value

solution_0 = get_best_friendship(relationships)

relationships["you"] = {}
for name,rels in relationships.items():
    if name == "you": continue
    relationships["you"][name] = 0
    rels["you"] = 0

solution_1 = get_best_friendship(relationships)


print(solution_0) # PART 1: 618
print(solution_1) # PART 2: 601
