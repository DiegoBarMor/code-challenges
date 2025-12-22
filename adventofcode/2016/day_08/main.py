import numpy as np

HSCREEN = 6
WSCREEN = 50

def formatarr(arr) -> str:
    return '\n'.join(''.join('#' if x else '.' for x in row) for row in arr)

def rect(arr, w, h):
    arr[:h, :w] = True

def rot_row(arr, row, by):
    by %= WSCREEN
    idxs = list(range(by, arr.shape[1])) + list(range(0, by)) # tested in python 3.12.12
    arr[row, idxs] = arr[row, :]

def rot_col(arr, col, by):
    by %= HSCREEN
    idxs = list(range(by, arr.shape[0])) + list(range(0, by)) # tested in python 3.12.12
    arr[idxs, col] = arr[:, col]

def parse(chars: str) -> tuple[callable, int, int]:
    parts = chars.strip().split()
    if parts[0] == "rect":
        arg0, arg1 = parts[1].split('x')
        return rect, int(arg0), int(arg1)

    assert parts[0] == "rotate", f"Unknown instruction: {parts[0]}"

    func = rot_row if parts[1] == "row" else rot_col
    arg0 = int(parts[2].split('=')[1])
    arg1 = int(parts[4])
    return func, arg0, arg1


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')


arr = np.zeros((HSCREEN, WSCREEN), dtype = bool)
for row in data:
    func, arg0, arg1 = parse(row)
    func(arr, arg0, arg1)

print(np.sum(arr)) # PART 1: 123
print(formatarr(arr)) # PART 2: AFBUPZBJPS
