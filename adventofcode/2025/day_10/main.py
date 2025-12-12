
def parse_tlights(chars: str):
    chars_01 = map(lambda c: '1' if c=='#' else '0', chars.strip("[]")[::-1])
    return int(''.join(chars_01), base = 2)

def parse_buttons(chars: str):
    set_ints = set(int(n) for n in chars.strip("()").split(','))
    chars_01 = map(lambda n: '1' if n in set_ints else '0', range(max(set_ints),-1,-1))
    return int(''.join(chars_01), base = 2)

def parse_joltage(chars: str):
    return tuple(map(int, chars.strip("{}").split(',')))

def iter_xor_combos(nums: list[int]):
    for i,n0 in enumerate(nums[:-1]):
        for n1 in nums[i+1:]:
            yield n0,n1,n0^n1


with open("input.txt", 'r') as file:
    data = [row.split() for row in file.read().strip().split('\n')]


ilights = [parse_tlights(row[0]) for row in data] # "indicator light diagrams"
buttons = [[parse_buttons(b) for b in row[1:-1]] for row in data] # "button wire schematics
joltage = [parse_joltage(row[-1]) for row in data] # "joltage requirements"


min_presses_ilights = 0
for ilight,btts in zip(ilights, buttons):
    presses = {b:1 for b in btts}
    while ilight not in presses:
        for n0,n1,nxor in iter_xor_combos(list(presses.keys())):
            oldval = presses.get(nxor, float("inf"))
            newval = presses[n0] + presses[n1]
            presses[nxor] = min(oldval, newval)
            if nxor == ilight: break

    min_presses_ilights += presses[ilight]

print(min_presses_ilights) # PART 1: 535
print() # PART 2:

# .... 0
# ...# 1
# ..#. 2
# ..## 3
# .#.. 4
# .#.# 5
# .##. 6
# .### 7
# #... 8
