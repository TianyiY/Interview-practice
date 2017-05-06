## implementing minimum spaning tree on graph

import numpy as np

#  minimum spanning tree
def question3(G):
    if len(G)==0:
        return 'Empty input'
    for i in range(len(G)):
        if len(G[G.keys()[i]])==0:
            return 'No connection'
    # initialize the minimum spanning tree of G
    G_MST = {}
    # initialize the first key
    G_MST[G.keys()[0]] = []

    # traverse until all the vertices have been reached
    while len(G_MST.keys()) < len(G.keys()):
        minWeight = np.inf  # record the minimum weight between two vertices, initialize as an infinite integer
        minEdge = None  # record the edge with minimum weight (two vertices)
        # traverse each key in G_MST
        for key in G_MST.keys():
            # find the new vertices and weights
            connection = [(weight, vertice) for (vertice, weight) in G[key] if vertice not in G_MST.keys()]
            # find the minimum weight and corresponding edge
            if len(connection) > 0:
                w, v = min(connection)
                if w < minWeight:
                    minWeight = w
                    minEdge = (key, v)
        # update my G minimun spanning tree
        G_MST[minEdge[0]].append((minEdge[1], minWeight))
        G_MST[minEdge[1]] = [(minEdge[0], minWeight)]
    return G_MST


# test
print question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]})

print question3({'A': [('B', 3), ('C', 4)],
 'B': [('A', 3), ('C', 5), ('D', 7), ('E', 8)],
 'C': [('A', 4), ('B', 5), ('D', 9), ('E', 6)],
 'D': [('B', 7), ('C', 9), ('E', 10)],
 'E': [('B', 8), ('C', 6), ('D', 10)]})

print question3({})
print question3({'A':['B, 3'], 'B':[]})





