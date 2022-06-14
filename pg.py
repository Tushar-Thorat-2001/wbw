import networkx as nx
import random
import numpy as np

def add_edges(g, pr):
    for each in g.nodes():
        for each1 in g.nodes():
            if (each != each1):
                ra = random.random()
                if (ra < pr): g.add_edge(each, each1)
            else:
                continue
    return g

def nodes_sorted(g, points):
    t = np.array(points)
    t= np.argsort(-t)
    return t

def random_Walk(g):
    rwp = [0 for i in range(g.number_of_nodes())]
    nodes = list(g.nodes())
    r = random.choice(nodes)
    rwp[r] += 1
    neigh = list(g.out_edges(r))
    z = 0

    while (z != 10000):
        if (len(neigh) == 0):
            focus = random.choice(nodes)
        else:
            r1 = random.choice(neigh)
            focus = r1[1]
            rwp[focus] += 1
            neigh = list(g.out_edges(focus))
            z += 1
    return rwp

g = nx.DiGraph()

N = 4
g.add_nodes_from(range(N))

g = add_edges(g, 0.4)
points = random_Walk(g)
sorted_by_points = nodes_sorted(g, points)
print("PageRank using Random Walk Method")
print(sorted_by_points)

#PageRank using Random Walk Method [2 3 0 1]


p_dict = nx.pagerank(g)
p_sort = sorted(p_dict.items(), key=lambda x: x[1], reverse=True)

print("PageRank using inbuilt pagerank method")
for i in p_sort:
    print(i[0], end=", ")

#PageRank using inbuilt pagerank method 2, 3, 0, 1,
