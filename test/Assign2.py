maxedgeweight = 100

import random


# Generates a graph as a dictionary, where
# The graph will have $n$ vertices and each edge has a chance p of being generated (but we ensure that
# we ensure that every vertex has at least an edge).
# If the edge exists, a weight is uniformly generated in {1,..., maxedgeweight}
def generateGraph(n, p, s):
    random.seed(s)
    G = {}
    for i in range(0, n):
        # we arbitrarily draw a vertex r different than i
        # and add one edge between i and r, so that every vertex has an edge
        r = (i + random.randint(1, n)) % n
        G[(min(i, r), max(i, r))] = random.randint(1, maxedgeweight + 1)
        for j in range(i + 1, n):
            if random.random() <= p and j != r:
                G[(i, j)] = random.randint(1, maxedgeweight + 1)
    return G

def getN(G):
    n = 0
    for key in G:
        if key[0] > n:
            n = key[0]
        if key[1] > n:
            n = key[1]
    n = n + 1
    return n

def printGraph(G):
    v = getN(G)
    matrix = [[]]*v

    for i in range(v):
        list = [0]*v
        matrix[i] = list

    for key in G:
        matrix[key[0]][key[1]] = G[key]

    return matrix


def maxDegree(G):
    maxdegree = 0
    # ............
    matrix = printGraph()


    return maxdegree

testG = generateGraph(5, 1, 11)
print(testG)
print(getN(testG))
print(printGraph(testG))

# The gun fight problem
G = {(0, 0): 0.43875, (0, 2): 0.23625, (0, 3): 0.21125, (0, 6): 0.11375, (2, 2): 0.63, (2, 4): 0.27, (2, 6): 0.07,
     (2, 7): 0.03, (3, 3): 0.68, (3, 5): 0.12, (3, 6): 0.17, (3, 7): 0.03}


def gunfightSimulation(G):
    state = 0
    track = [0]
    while state not in [4, 5, 6, 7]:
        if state == 0:
            state = random.choice([0, 2, 3, 6])
            track.append(state)
        elif state == 2:
            state = random.choice([2, 4, 6, 7])
            track.append(state)
        elif state == 3:
            state = random.choice([3, 4, 5, 7])
            track.append(state)

    print(track)
    return state

    # print(gunfightSimulation(G))
