from collections import defaultdict
 
# This class represents an directed graph
# using adjacency list representation
 # class Graph is taken from GeeksForGeeks 
#https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
 
class Graph:
 
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
        self.Time = 0
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #All code under this comment is made by me 
        
    