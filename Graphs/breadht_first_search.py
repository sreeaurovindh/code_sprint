from collections import DefaultDict

class Graph:
    def __init__(self,num_nodes):
        self.graph = DefaultDict(list)
        self.num_nodes = num_nodes
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def b
