def bitmask(num: int): return num & 0xFFFF

class Node:
    def __init__(self):
        self.src0: "Node" = None
        self.src1: "Node" = None
        self.value: "int" = None

    def set_sources(self, src0, src1):
        self.src0 = src0
        self.src1 = src1

    def set_value(self, val):
        self.value = val

    def get_value(self) -> int:
        if self.value is None:
            self.value = self._calc_val()
        return self.value

    def reset(self):
        self.value = None

    def _calc_val(self):
        raise NotImplementedError()

class Source(Node):
    def __init__(self, value: int):
        super().__init__()
        self.set_value(value)

    def get_value(self) -> int:
        return self.value

class IdentityGate(Node):
    def _calc_val(self) -> int:
        return self.src0.get_value()

class NotGate(Node):
    def _calc_val(self) -> int:
        return bitmask(~self.src0.get_value())

class AndGate(Node):
    def _calc_val(self) -> int:
        return bitmask(self.src0.get_value() & self.src1.get_value())

class OrGate(Node):
    def _calc_val(self) -> int:
        return bitmask(self.src0.get_value() | self.src1.get_value())

class LshiftGate(Node):
    def _calc_val(self) -> int:
        return bitmask(self.src0.get_value() << self.src1.get_value())

class RshiftGate(Node):
    def _calc_val(self) -> int:
        return bitmask(self.src0.get_value() >> self.src1.get_value())

SOURCES: dict[str, Source] = {}
STR2CLASS = {
    "AND": AndGate,
    "OR": OrGate,
    "LSHIFT": LshiftGate,
    "RSHIFT": RshiftGate,
}

def parse(chars: str) -> tuple[str, Node, "str", "str"]:
    inp,name = chars.strip().split(" -> ")
    parts = inp.split()

    for part in parts:
        if part.isnumeric() and part not in SOURCES:
            SOURCES[part] = Source(value = int(part))

    if len(parts) == 1:
        return name, IdentityGate(), inp, ''

    if parts[0] == "NOT":
        return name, NotGate(), parts[1], ''

    cls_node = STR2CLASS[parts[1]]
    return name, cls_node(), parts[0], parts[2]


with open("input.txt", 'r') as file:
    data = file.read().strip().split('\n')


names, nodes, str0s, str1s = zip(*(parse(row) for row in data))
graph = {name:node for name,node in zip(names,nodes)}
assert len(nodes) == len(graph)

graph.update(SOURCES)

for node,str0,str1 in zip(nodes, str0s, str1s):
    if isinstance(node, Source): continue
    src0 = graph[str0]
    src1 = graph.get(str1)
    node.set_sources(src0, src1)

target_node = graph['a']
result_0 = target_node.get_value()

for node in nodes: node.reset()
graph['b'].set_value(result_0)
result_1 = target_node.get_value()


print(result_0) # PART 1: 3176
print(result_1) # PART 2: 14710
