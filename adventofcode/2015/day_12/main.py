import re, json

with open("input.txt", 'r') as file:
    data = file.read().strip()

sum_nums_all = sum(map(int, re.findall(r"-?\d+", data)))
sum_nums_nored = 0

node = json.loads(data)
queue = [node]
while queue:
    node = queue.pop()
    if isinstance(node, list):
        queue.extend(node)

    elif isinstance(node, dict):
        if "red" in node.values(): continue
        queue.extend(node.values())

    elif isinstance(node, int):
        sum_nums_nored += node

print(sum_nums_all)   # PART 1: 156366
print(sum_nums_nored) # PART 2: 96852
