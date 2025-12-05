from collections import defaultdict

with open("input.txt", 'r') as file:
    data = file.read().strip()


raw_ranges,raw_ids = data.strip().split("\n\n")

ids = [int(n) for n in raw_ids.split()]

dict_ranges = defaultdict(int)
for row in raw_ranges.split():
    i0,i1 = row.split('-')
    i0,i1 = int(i0), int(i1)
    dict_ranges[i0] = max(dict_ranges[i0], i1)

marked_delete = set()
keys_ranges = sorted(dict_ranges.keys())

for idx,i0 in enumerate(keys_ranges[:-1]):
    for j0 in keys_ranges[idx+1:]: # implies j0 > i0
        if j0 in marked_delete: continue
        i1 = dict_ranges[i0]
        j1 = dict_ranges[j0]

        if j1 <= i1:              # CASE 1: i0--------i1
            marked_delete.add(j0) #            j0--j1
            continue

        if j0 <= i1:              # CASE 2: i0--------i1
            dict_ranges[i0] = j1  #              j0-------j1
            marked_delete.add(j0)
            continue

        ### CASE 3: i0----i1
        ###                   j0----j1
        break

for j0 in marked_delete: del dict_ranges[j0]


count_fresh = 0
for n in ids:
    for i0,i1 in dict_ranges.items():
        if n < i0: continue
        if n > i1: continue
        count_fresh += 1
        break

max_possible_fresh = 0
for i0,i1 in dict_ranges.items():
    max_possible_fresh += i1 - i0 + 1


print(count_fresh) # PART 1: 613
print(max_possible_fresh) # PART 2: 336495597913098
