import math

with open("input.txt", 'r') as file:
    data = file.read().strip('\n').split('\n')

def map_op(c: str) -> "callable | None":
    if c == '+': return sum
    if c == '*': return math.prod

def iter_v0(data):
    lst_nums = zip(*(row.strip().split() for row in data[:-1]))
    lst_ops  = map(map_op, data[-1].strip().split())
    return zip(lst_nums, lst_ops)

def iter_v1(data):
    nums = []
    for column in reversed(tuple(zip(*data))):
        n = ''.join(column[:-1]).strip()
        if not n:
            nums = []; continue

        nums.append(n)
        op = map_op(column[-1])
        if op is None: continue
        yield nums, op

def get_total(obj_iter):
    return sum(
        op(int(n) for n in nums) for nums,op in obj_iter
    )

lst_nums = zip(*(row.strip().split() for row in data[:-1]))
lst_ops  = map(map_op, data[-1].strip().split())

print(get_total(iter_v0(data))) # PART 1: 7098065460541
print(get_total(iter_v1(data))) # PART 2: 13807151830618
