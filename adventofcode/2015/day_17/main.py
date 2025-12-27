from collections import defaultdict

def iter_selection_masks(n: int):
    if not n:
        yield (); return

    for mask in iter_selection_masks(n-1):
        yield (True,)  + mask
        yield (False,) + mask

TARGET = 150

with open("input.txt", 'r') as file:
    data = file.read().strip().split()

containers = list(map(int, data))
nvalidconts = defaultdict(int)
for combo in iter_selection_masks(len(containers)):
    csum = sum(cont * int(comb) for cont,comb in zip(containers, combo))
    if csum != TARGET: continue
    nvalidconts[sum(combo)] += 1

possibilities = sum(nvalidconts.values())
nmin_conts = min(nvalidconts.items(), key = lambda t: t[0])[1]

print(possibilities) # PART 1: 1638
print(nmin_conts)    # PART 2: 17
