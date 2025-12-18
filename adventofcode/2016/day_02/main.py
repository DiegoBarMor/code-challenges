CHAR2VEC = {
    'U': (-1, 0),
    'R': ( 0, 1),
    'D': ( 1, 0),
    'L': ( 0,-1),
}

BUTTONS_0 = [
    ['',  '',  '',  '', ''],
    ['', '1', '2', '3', ''],
    ['', '4', '5', '6', ''],
    ['', '7', '8', '9', ''],
    ['',  '',  '',  '', ''],
]

BUTTONS_1 = [
    ['',  '',  '',  '',  '',  '', ''],
    ['',  '',  '', '1',  '',  '', ''],
    ['',  '', '2', '3', '4',  '', ''],
    ['', '5', '6', '7', '8', '9', ''],
    ['',  '', 'A', 'B', 'C',  '', ''],
    ['',  '',  '', 'D',  '',  '', ''],
    ['',  '',  '',  '',  '',  '', ''],
]

def navigate_keypad(buttons: list[list[str]], pos_init: tuple[int, int]):
    pressed = ''
    py,px = pos_init
    for row in data:
        for c in row:
            dy,dx = CHAR2VEC[c]
            newpy = py + dy
            newpx = px + dx
            if buttons[newpy][newpx]:
                py = newpy
                px = newpx
        pressed += buttons[py][px]
    return pressed


with open("input.txt", 'r') as file:
    data = file.read().strip().split()


print(navigate_keypad(BUTTONS_0, pos_init = (2,2))) # PART 1: 44558
print(navigate_keypad(BUTTONS_1, pos_init = (3,1))) # PART 2: 6BBAD
