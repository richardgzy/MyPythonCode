class Vertex:
    def __init__(self, key, weight):
        """A Vertex has an id and a set of neighbours."""
        self.id = key
        self.weight = weight
        self.connectedTo = set()

    def addNeighbour(self, nbr):
        """
        Add a neighbour.

        Parameters:

            - nbr: id of the neighbour
        """
        self.connectedTo.add(nbr)

    def hasNeighbour(self, nbr):
        """
        Check for a neighbour.

        Parameters:

            - nbr: id of the potential neighbour

        Returns: Whether `nbr` is a neighbour
        """
        if nbr in self.connectedTo:
            return True

        return False

    # Getters
    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.id

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + ", ".join(
            [str(i) for i in self.connectedTo])


class Graph:
    def __init__(self):
        """A graph is a dictionary of {id: vertex}."""
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key, weight):
        """Add a vertex if it does not exist yet."""
        newVertex = None

        if key not in self.vertList:
            self.numVertices = self.numVertices + 1
            newVertex = Vertex(key, weight)
            self.vertList[key] = newVertex

        return newVertex

    def addEdge(self, f, t):
        """
        Add an edge between two existing vertices.

        Parameters:

            - f: id of the first vertex

            - t: id of the second vertex

        Returns: True if an edge was added; otherwise False
        """
        if f in self.vertList and t in self.vertList:
            self.vertList[f].addNeighbour(t)
            self.vertList[t].addNeighbour(f)

            return True
        else:
            return False

    def hasEdge(self, i, j):
        """
        Check whether nodes `i` and `j` are connected.

        Parameters:

            - i: id of the first node

            - j: id of the second node

        Returns: whether edge (i, j) exists or not
        """
        if i.hasNeighbour(j):
            return True
        return False

    # Getters
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.values()

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        return "\n".join([str(v) for v in self.vertList.values()])

