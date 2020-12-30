from collections import defaultdict

class SimpleGraph(object):
    """docstring for SimpleGraph."""
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,element,visited):
        # we have not visited this node before Hence we don't have to check
        # for this condition.
        visited[element] = True
        print(element)
        for node in self.graph[element]:
            if visited[node] == False:
                self. DFSUtil(node,visited)





    def DFS(self):
        print(self.graph)
        visited = [False] * len(self.graph)
        for node in self.graph.keys():
            if visited[node] == False:
                self.DFSUtil(node,visited)


g = SimpleGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS()
