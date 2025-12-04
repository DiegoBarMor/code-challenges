def get_max(s):
    """returns first occurance of the maximum value"""
    return max(enumerate(s), key = lambda t: t[1])

def find_max_substring(line: str, chunksize: int) -> str:
    section = line
    max_substring = ""
    for j in range(1,chunksize+1):
        idx_end = len(section) - chunksize + j
        i1,v1 = get_max(section[:idx_end])
        section = section[i1+1:]
        max_substring += v1
    return max_substring

def sum_max_substrings(lines: list[str], chunksize: int) -> int:
    return sum(int(find_max_substring(b, chunksize)) for b in banks)

with open("input.txt", 'r') as file:
    banks = [b.strip() for b in file.read().strip().split()]

print(sum_max_substrings(banks, chunksize =  2)) # PART 1: 17359
print(sum_max_substrings(banks, chunksize = 12)) # PART 2: 172787336861064
