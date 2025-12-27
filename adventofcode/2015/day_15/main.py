class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    @classmethod
    def parse(cls, chars: str):
        name, prop = chars.strip().split(':')
        properties = (int(p.split()[1]) for p in prop.split(','))
        return cls(name, *properties)

    def multiply(self, n: int):
        return Ingredient(self.name,
            n * self.capacity,
            n * self.durability,
            n * self.flavor,
            n * self.texture,
            n * self.calories,
        )

def iterate_integer_partitions(k: int, total: int):
    if k == 1:
        yield (total,); return

    for n in range(total+1):
        for c in iterate_integer_partitions(k-1, total-n):
            yield c + (n,)

def cookie_score(ings: list[Ingredient]):
    cap = max(0, sum(ing.capacity   for ing in ings))
    dur = max(0, sum(ing.durability for ing in ings))
    fla = max(0, sum(ing.flavor     for ing in ings))
    tex = max(0, sum(ing.texture    for ing in ings))
    return cap * dur * fla * tex


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

NTOTAL   = 100
CALORIES = 500

ingredients = [Ingredient.parse(row) for row in data]
max_score_all = 0
max_score_cal = 0
for combo in iterate_integer_partitions(len(data), NTOTAL):
    ings = [ing.multiply(mul) for mul,ing in zip(combo, ingredients)]
    score = cookie_score(ings)
    max_score_all = max(max_score_all, score)
    if sum(ing.calories for ing in ings) != CALORIES: continue
    max_score_cal = max(max_score_cal, score)

print(max_score_all) # PART 1: 21367368
print(max_score_cal) # PART 2: 1766400
