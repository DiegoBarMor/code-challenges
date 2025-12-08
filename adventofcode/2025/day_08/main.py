import numpy as np
import math

# NCONNECTIONS = 10 # for "example.txt"
NCONNECTIONS = 1000 # for "input.txt"
NLARGESTCLUSTERS = 3

class Node:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.pos = np.array([self.x, self.y, self.z])
        self.edges: "list[Node]" = []

    def add_edge(self, other: "Node"):
        self.edges.append(other)

    @staticmethod
    def distance(n0: "Node", n1: "Node"):
        return np.linalg.norm(n1.pos - n0.pos)


def calc_prod_n_largest_clusters(nodes):
    clusters = []
    used_nodes = set()
    for node in nodes:
        if node in used_nodes: continue

        cluster = set()
        queue = [node]
        while queue:
            n0 = queue.pop()
            if n0 in used_nodes: continue
            used_nodes.add(n0)
            cluster.add(n0)

            for n1 in n0.edges:
                if n1 in used_nodes: continue
                queue.append(n1)
                cluster.add(n1)

        clusters.append(cluster)

    cluster_sizes = sorted((len(c) for c in clusters), reverse = True)
    return math.prod(cluster_sizes[:NLARGESTCLUSTERS])


with open("input.txt", 'r') as file:
    data = file.read().strip().split()


nodes = [Node(*row.split(',')) for row in data]
mat_dist = np.tril(np.array(
    [[Node.distance(obj0, obj1) for obj1 in nodes] for obj0 in nodes]
))
mat_dist[mat_dist == 0] = np.inf

iteration = 1
used_nodes = set()
prod_large_clusters = None
prod_last_node_pair = None

while not np.all(mat_dist == np.inf):
    idx_flat = np.argmin(mat_dist)
    idx0 = idx_flat // len(nodes)
    idx1 = idx_flat %  len(nodes)

    node0 = nodes[idx0]
    node1 = nodes[idx1]
    node0.add_edge(node1)
    node1.add_edge(node0)
    mat_dist[idx0, idx1] = np.inf

    used_nodes.add(node0)
    used_nodes.add(node1)

    if len(used_nodes) == len(nodes):
        prod_last_node_pair = node0.x * node1.x
        break

    if prod_large_clusters is None and (iteration % NCONNECTIONS) == 0:
        prod_large_clusters = calc_prod_n_largest_clusters(nodes)

    iteration += 1


print(prod_large_clusters) # PART 1: 63920
print(prod_last_node_pair) # PART 2: 1026594680
