import math
 
class Node:
    def __init__(self,u):
       self.u = u
       self.v = []
       self.low = math.inf
       self.disc = 0
       self.parent = None
       
    def add_Edge(self, e):
        self.v.append(e)

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append([])
        
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    #All code under this comment is made by me 
        
new = Graph(8)
edges = [[1,2],[2,3],[3,4],[4,1],[2,4],[3,5],[5,6],[5,7],[5,8]]

for i in edges:
    new.addEdge(i[0] - 1,i[1])
    new.addEdge(i[1] - 1, i[0])

print(new.graph)