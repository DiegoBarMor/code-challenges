from collections import Counter
from string import ascii_lowercase

def parse(row: str) -> tuple[str,int,str]:
    substr,checksum = row.rstrip(']').split('[')
    substr_split = substr.split('-')
    encoded = substr_split[:-1]
    sector  = substr_split[-1]
    return '-'.join(encoded), int(sector), checksum

def validate(room: tuple[str,int,str]) -> int:
    encoded,sector,csumtarget = room
    count = Counter(encoded); del count['-']
    count = sorted(count.items(), key = lambda t: (-t[1], t[0]))
    checksum = ''.join(t[0] for t in count[:5])
    return sector if checksum == csumtarget else 0

def decrypt(room: tuple[str,int,str]) -> str:
    encoded,sector,_ = room
    nshift = sector % len(ascii_lowercase)
    shifted_ascii = ascii_lowercase[nshift:] + ascii_lowercase[:nshift]
    shifter = dict(zip(ascii_lowercase, shifted_ascii))
    shifter['-'] = ' '
    return ''.join(map(lambda c: shifter[c], encoded))


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')


rooms = list(map(parse, data))
sum_sectors = sum(map(validate, rooms))

for room in rooms:
    if "northpole" in decrypt(room):
        sector_npstorage = room[1]
        break

print(sum_sectors) # PART 1: 137896
print(sector_npstorage) # PART 2: 501
