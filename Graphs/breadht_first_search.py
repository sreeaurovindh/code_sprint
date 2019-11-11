class Graph:
    def __init__(self,num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def b
