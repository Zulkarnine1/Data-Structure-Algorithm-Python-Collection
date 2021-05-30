# Class Graph

# attr no. of nodes
# adjacent list

# functions -
# 1. addVertex
# 2. addEdge
# 3. show graph

class Graph:

    def __init__(self):
        self.numofnodes = 0
        self.adjList = {}

    def addVertex(self, node):
        if node not in self.adjList:
            self.adjList[node] = []
            self.numofnodes += 1
            return node
        else:
            return None

    def addEdge(self,node1,node2):
        self.adjList[node1].append(node2)
        self.adjList[node2].append(node1)
        return True


    def showGraph(self):
        print(self.adjList)


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showGraph()