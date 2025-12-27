def look_and_say(chars: str):
    count = 0
    out = ""
    current_char = chars[0]
    for c in chars:
        if c == current_char:
            count += 1; continue
        out += f"{count}{current_char}"
        current_char = c
        count = 1
    return out + f"{count}{current_char}"

def n_look_and_say(chars: str, n: int):
    for _ in range(n):
        chars = look_and_say(chars)
    return chars


with open("input.txt", 'r') as file:
    data = file.read().strip()

print(len(n_look_and_say(data, 40))) # PART 1: 329356
print(len(n_look_and_say(data, 50))) # PART 2: 4666278
