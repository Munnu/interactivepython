class Vertex:
    """ Uses a dictionary to keep track of the vertices
        to which it is connected, and the weight of each edge
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + \
            str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo(neighbor)

class Graph:
    """ Holds master list of all vertices """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, from_v, to_v, cost=0):
        if from_v not in self.vertList:
            nv = self.addVertex(from_v)
        if to_v not in self.vertList:
            new_v = self.addVertex(to_v)
        self.vertList[from_v].addNeighbor(self.vertList[to_v], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# example of how this thing works
g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for vertex in g:
    for weight in vertex.getConnections():
        print "(%s, %s)" % (vertex.getId(), weight.getId())
