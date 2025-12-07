import numpy as np

class MatRange:
    def __init__(self, i0, i1, j0, j1):
        self.i0 = int(i0)
        self.i1 = int(i1) + 1
        self.j0 = int(j0)
        self.j1 = int(j1) + 1

    def __str__(self):
        return f"{self.i0}:{self.i1},{self.j0}:{self.j1}"

class Lights:
    def __init__(self, data):
        self._arr = np.zeros((1000, 1000), dtype = bool)
        self._instructions = data

    def calc_brightness(self):
        for instr in self._instructions:
            op = self._parse_operation(instr)
            mrange = self._parse_matrange(instr)
            op(mrange)
        return np.sum(self._arr)

    def _turn_on(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1] = True

    def _turn_off(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1] = False

    def _toggle(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1] =\
            ~self._arr[r.i0:r.i1, r.j0:r.j1]

    def _parse_operation(self, line: str):
        if line.startswith("turn on"):  return self._turn_on
        if line.startswith("turn off"): return self._turn_off
        if line.startswith("toggle"):   return self._toggle
        raise ValueError(f"Unknown operation in '{line}'")

    def _parse_matrange(self, line: str) -> MatRange:
        s_, s1 = line.split(" through ")
        s0 = s_.split()[-1]
        i0,j0 = s0.split(',')
        i1,j1 = s1.split(',')
        return MatRange(i0 = i0, i1 = i1, j0 = j0, j1 = j1)

class LightsAlt(Lights):
    def __init__(self, data):
        self._arr = np.zeros((1000, 1000), dtype = int)
        self._instructions = data

    def _turn_on(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1] += 1

    def _turn_off(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1][
            self._arr[r.i0:r.i1, r.j0:r.j1] > 0
        ] -= 1

    def _toggle(self, r: MatRange):
        self._arr[r.i0:r.i1, r.j0:r.j1] += 2


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')


print(Lights   (data).calc_brightness()) # PART 1: 543903
print(LightsAlt(data).calc_brightness()) # PART 2: 14687245
