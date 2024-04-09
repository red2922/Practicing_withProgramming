import math
 
class Node:
    def __init__(self,u):
       self.u = u
       self.v = []
       self.low = math.inf
       self.disc = -1
       self.parent = None
       
    def add_Edge(self, e):
        self.v.append(e)

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append(Node(i+1))
        
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].add_Edge(v)

def dfs(g ,v, stack):
    current = g.graph[v - 1]
    current.disc = time
    current.low = time

    for i in current.v:
        if i.disc == -1:
            stack.append(i,current.u)
            g.graph[i - 1].parent = i

            return dfs(g,v, stack)
            








new = Graph(8)
edges = [[1,2],[2,3],[3,4],[4,1],[2,4],[3,5],[5,6],[5,7],[5,8]]

for i in edges:
    new.addEdge(i[0] - 1,i[1])
    new.addEdge(i[1] - 1, i[0])

"""for i in new.graph:
    print(i.u)
    print(i.v)"""

stack = []
time = 0


