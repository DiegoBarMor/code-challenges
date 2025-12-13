def sum_equals_in(arr0, arr1):
    mask = (c0 == c1 for c0,c1 in zip(arr0, arr1))
    return sum(int(data[i]) for i,b in enumerate(mask) if b)

with open("input.txt", 'r') as file:
    data = file.read().strip()

sol0 = sum_equals_in(data, data[1:] + data[0])
sol1 = sum_equals_in(data[:len(data)//2 ], data[ len(data)//2:]) +\
       sum_equals_in(data[ len(data)//2:], data[:len(data)//2 ])

print(sol0) # PART 1: 1171
print(sol1) # PART 2: 1024
