from collections import defaultdict
# Try to find if a graph has cycle we have to check if there is a backedge
# in the graph. So, inorder to do this 

class Graph:
    def __init__(self,num_nodes):
        self.graph= defaultdict(list)
        self.num_nodes = num_nodes
    def addEdge(self,u,v):
        self.graph[u]= v

    def is_cyclic_util(self,v,visited,recStack):
        visited[v]= True
        recStack[v] = True

        for neighbor in graph[v]:
            if v not in visited:
                if self.is_cyclic_util(self,neighbor,visited,recStack) == True
