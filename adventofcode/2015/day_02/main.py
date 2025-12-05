with open("input.txt", 'r') as file:
    data = file.read().strip().split()

total_paper = 0
total_ribbon = 0
for dimensions in data:
    l,w,h = (int(n) for n in dimensions.split('x'))
    perim_lw = 2*(l + w)
    perim_wh = 2*(w + h)
    perim_lh = 2*(l + h)
    area_lw  = l * w
    area_wh  = w * h
    area_lh  = l * h
    volume   = area_lw*h

    paper = 2 * (area_lw + area_wh + area_lh)
    slack = min(area_lw, area_wh, area_lh)
    total_paper += paper + slack

    ribbon = min(perim_lw, perim_wh, perim_lh)
    bow = volume
    total_ribbon += ribbon + bow

print(total_paper)  # PART 1: 1606483
print(total_ribbon) # PART 2: 3842356
