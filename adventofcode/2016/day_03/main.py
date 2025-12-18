def is_valid_triangle(a: int, b: int, c: int):
    return (a+b>c) and (a+c>b) and (b+c>a)

with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

lines = [
    tuple(map(int, row.strip().split()))
    for row in data
]

nvalids_rows = sum(is_valid_triangle(*ls) for ls in lines)

nvalids_cols = 0
for long_tuple in zip(*lines):
    chunks = (long_tuple[3*i:3*(i+1)] for i in range(len(long_tuple)//3))
    nvalids_cols += sum(is_valid_triangle(*ls) for ls in chunks)


print(nvalids_rows) # PART 1: 869
print(nvalids_cols) # PART 2: 1544
