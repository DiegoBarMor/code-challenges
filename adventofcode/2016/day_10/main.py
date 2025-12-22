class Container:
    def __init__(self, idx: int):
        self.idx = idx
        self.chips: list[int] = []

    def take(self, chip: int):
        self.chips.append(chip)


class Bin(Container): pass


class Bot(Container):
    def __init__(self, idx):
        super().__init__(idx)
        self.outlow:  Container = None
        self.outhigh: Container = None

    def can_give(self) -> bool:
        return len(self.chips) == 2

    def get_sorted_chips(self):
        return sorted(self.chips)

    def take(self, chip: int):
        assert len(self.chips) < 2
        super().take(chip)

    def give(self):
        if not self.can_give(): return None, None
        low, high = self.get_sorted_chips()
        self.outlow.take(low)
        self.outhigh.take(high)
        self.chips.clear()
        return low, high


def parse_take(chars: str):
    _, chip, _, _, _, idx_bot = chars.split()
    return int(chip), int(idx_bot)

def parse_give(chars: str):
    _, idx_bot, _, _, _, kind_outlow, idx_outlow, \
        _, _, _, kind_outhigh, idx_outhigh = chars.split()
    return map(int, (
        idx_bot, kind_outlow == "bot", idx_outlow, kind_outhigh == "bot", idx_outhigh
    ))


with open("input.txt", 'r') as file:
    data_raw = file.read().strip()


data = data_raw.split('\n')
instrs_take = filter(lambda s: s.startswith("value"), data)
instrs_give = sorted(filter(lambda s: s.startswith("bot"), data), key = lambda s: int(s.split()[1]))

bots = [Bot(i) for i,_ in enumerate(instrs_give)] # assume each bot gives its chips exactly once
bins = [Bin(i) for i in range(data_raw.count("output"))] # assume each output bin appears only once in the instructions

for instr in instrs_take:
    chip, idx_bot = parse_take(instr)
    bots[idx_bot].take(chip)

for instr in instrs_give:
    idx_bot, isbot_outlow, idx_outlow, isbot_outhigh, idx_outhigh = parse_give(instr)
    bot = bots[idx_bot]
    bot.outlow  = (bots if isbot_outlow  else bins)[idx_outlow ]
    bot.outhigh = (bots if isbot_outhigh else bins)[idx_outhigh]


bot_61_17 = None
while any(map(Bot.can_give, bots)):
    for bot in bots:
        low, high = bot.give()
        if bot_61_17 is None and low == 17 and high == 61:
            bot_61_17 = bot
product_bins = bins[0].chips[0] * bins[1].chips[0] * bins[2].chips[0]


print(bot_61_17.idx) # PART 1: 116
print(product_bins)  # PART 2: 23903
