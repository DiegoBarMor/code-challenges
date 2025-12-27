import re

class Reindeer:
    def __init__(self, chars: str):
        pattern = r"^(?P<name>\w+).+ (?P<speed>\d+) km/s.+ (?P<trun>\d+) seconds,.+ (?P<trest>\d+) seconds\.$"
        m = re.fullmatch(pattern, chars)
        self.name   = m.group("name")
        self.speed  = int(m.group("speed"))
        self.t_run  = int(m.group("trun"))
        self.t_rest = int(m.group("trest"))
        self.points = 0
        self.distance = 0
        self.dists: list[int] = []

    def reset(self):
        self.points = 0
        self.distance = 0
        self.dists.clear()

    def run_simple(self, seconds: int):
        elapsed = 0
        resting = False
        while elapsed < seconds:
            if resting:
                dt = self.t_rest
            else:
                dt = min(self.t_run, seconds - elapsed)
                self.distance += dt * self.speed
            elapsed += dt
            resting = not resting

    def run_detailed(self, seconds: int):
        dist = 0
        partial = 0
        resting = False
        for _ in range(seconds):
            if resting:
                t = self.t_rest
            else:
                t = self.t_run
                dist += self.speed
            partial += 1
            self.dists.append(dist)
            if partial != t: continue
            partial = 0
            resting = not resting

SECONDS = 2503

with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')

reindeers = [Reindeer(row) for row in data]
for r in reindeers: r.run_simple(SECONDS)
winning_dist = max(r.distance for r in reindeers)

for r in reindeers: r.reset()
for r in reindeers: r.run_detailed(SECONDS)

for i in range(SECONDS):
    max_dist = max(r.dists[i] for r in reindeers)
    for r in filter(lambda r: r.dists[i] == max_dist, reindeers):
        r.points += 1

winning_points = max(r.points for r in reindeers)

print(winning_dist)   # PART 1: 2696
print(winning_points) # PART 2: 1084
