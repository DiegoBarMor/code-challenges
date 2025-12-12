class Node:
    def __init__(self, name):
        self.name = name
        self.npaths = 0
        self.unaccessible = False
        self.children: "list[Node]" = []
        self.parents:  "list[Node]" = []

    def __repr__(self):
        return f"({len(self.parents)}->{self.name}->{len(self.children)}:{self.npaths})"

    def add_child(self, child: "Node"):
        self.children.append(child)
        child.parents.append(self)

    def forward(self):
        return iter(self.children)

    def backward(self):
        return iter(self.parents)

    def has_directed_path(self, dest: "Node"):
        queue = set([self])
        while queue:
            node = queue.pop()
            if node is dest: return True
            queue.update(node.forward())
        return False


class Graph:
    def __init__(self, data: str):
        self.nodes = {name: Node(name) for name in set(data.replace(':', '').split())}
        for row in data.split('\n'):
            name_src, names_dests = row.split(": ")
            node = self.nodes[name_src]
            for name in names_dests.split():
                node.add_child(self.nodes[name])

        self.SRC0    = self.nodes["you"]
        self.SRC1    = self.nodes["svr"]
        self.SINK    = self.nodes["out"]
        self.TARGET0 = self.nodes["dac"]
        self.TARGET1 = self.nodes["fft"]

    def __repr__(self):
        nedges = sum(len(node.children) for node in self.nodes.values())
        return f"Graph with {len(self.nodes)} nodes, {nedges} edges"

    def calc_npaths(self, src: Node, dest: Node, neighs: callable):
        for node in self.nodes.values(): node.npaths = 0
        queue = [src]
        while queue:
            node = queue.pop() # DFS
            node.npaths += 1
            queue.extend(neighs(node))
        return dest.npaths

    def trim(self):
        trimmed = {}
        for name,node in self.nodes.items():
            if node.unaccessible: continue
            trimmed[name] = node
            node.children = [n for n in node.children if not n.unaccessible]
            node.parents  = [n for n in node.parents  if not n.unaccessible]
        self.nodes = trimmed


with open("input.txt", 'r') as file:
    data = file.read().strip()


graph = Graph(data)
npaths_src0_sink = graph.calc_npaths(graph.SRC0, graph.SINK, Node.forward)

tsrc, tdest = (graph.TARGET0, graph.TARGET1) if \
    graph.TARGET0.has_directed_path(graph.TARGET1) \
    else (graph.TARGET1, graph.TARGET0)

npaths_src1_tsrc = graph.calc_npaths(tsrc, graph.SRC1, Node.backward)
npaths_tdest_sink = graph.calc_npaths(tdest, graph.SINK, Node.forward)

for node in graph.nodes.values():
    node.unaccessible = not (tsrc.has_directed_path(node) and node.has_directed_path(tdest))

graph.trim()

npaths_tsrc_tdest = graph.calc_npaths(tsrc, tdest, Node.forward)

print(npaths_src0_sink) # PART 1: 543
print(npaths_src1_tsrc*npaths_tsrc_tdest*npaths_tdest_sink) # PART 2: 479511112939968
# npaths_src1_tsrc = 2588
# npaths_tsrc_tdest = 18007824
# npaths_tdest_sink = 10289
