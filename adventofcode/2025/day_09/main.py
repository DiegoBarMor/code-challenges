import numpy as np

# 0!1 4!!5
# !.! !..!
# !.2!3..!
# !......!
# 7!!!!!!6
# 40, 24
toy = """
1,1
3,1
3,3
5,3
5,1
8,1
8,5
1,5
"""

# ..............
# .......0...1..
# ..............
# ..6....7......
# ..............
# ..5......4....
# ..............
# .........3.2..
# ..............    SOL: 4-6

example = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("input.txt", 'r') as file:
    data = file.read().strip().split()

#### non-numpy answer for part 1
# xlst, ylst = zip(*(row.split(',') for row in data))
# coords = [(int(x), int(y)) for x,y in zip(xlst,ylst)]
# rects = [
#     [
#         (abs(x1-x0)+1)*(abs(y1-y0)+1)*(i!=j)
#         for j,(x1,y1) in enumerate(coords)
#     ]   for i,(x0,y0) in enumerate(coords)
# ]
# max_area = max(max(row) for row in rects)

xlst, ylst = zip(*(row.split(',') for row in data))
coords = np.array(tuple(zip(xlst,ylst)), dtype = int)

tx0 = np.tile(coords[:,0], (len(data), 1))
ty0 = np.tile(coords[:,1], (len(data), 1))
tx1 = tx0.T
ty1 = ty0.T

rects = (np.abs(tx1-tx0)+1)*(np.abs(ty1-ty0)+1)
max_area = np.max(rects)

rects = np.tril(rects)
mask = np.zeros_like(rects, dtype = bool)

txmin = np.minimum(tx0, tx1)
tymin = np.minimum(ty0, ty1)
txmax = np.maximum(tx0, tx1)
tymax = np.maximum(ty0, ty1)

hlines = []; vlines = []
for i,(px0,py0) in enumerate(coords): # TODO: cleanup this
    if i == len(coords) - 1: i = -1
    px1,py1 = coords[i+1]
    if px0==px1:
        vlines.append((px0,py0,py1))
    else:
        hlines.append((py0,px0,px1))

for px,py0,py1 in vlines:
    py0,py1 = sorted((py0,py1))
    x_in = (txmin<px)&(px<txmax)
    y_in = ((py0<=tymin)&(tymax<=py1)) | ((tymin<py0)&(py0<tymax)) | ((tymin<py1)&(py1<tymax))
    mask |= x_in & y_in

for py,px0,px1 in hlines:
    px0,px1 = sorted((px0,px1))
    x_in = ((px0<=txmin)&(txmax<=px1)) | ((txmin<px0)&(px0<txmax)) | ((txmin<px1)&(px1<txmax))
    y_in = (tymin<py)&(py<tymax)
    mask |= x_in & y_in

for px,py in coords:
    x_in = (txmin<px)&(px<txmax)
    y_in = (tymin<py)&(py<tymax)
    p_in = x_in & y_in
    mask |= x_in & y_in


print(max_area) # PART 1: 4756718172
print(np.max(rects[~mask])) # PART 2: 1665679194


# from matplotlib import pyplot as plt
# rects[mask] = 0
# idx = np.argmax(rects)
# j = idx // len(coords)
# i = idx %  len(coords)
# plt.plot(coords[:,0], coords[:,1], marker = '.')
# plt.plot(
#     [coords[i,0], coords[i,0], coords[j,0], coords[j,0], coords[i,0]],
#     [coords[i,1], coords[j,1], coords[j,1], coords[i,1], coords[i,1]],
#     marker = 'x', linestyle = "--"
# )
# plt.gca().invert_yaxis()
# plt.show()
