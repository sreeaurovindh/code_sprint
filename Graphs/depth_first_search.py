from collections import defaultdict
class Graph:
    ```
    This function creates a graph 
    ```
    def __init__(self,num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs_iterative(self):
        stack = [0]
        visited = []
        while stack:
            element = stack.pop()
            if element not in visited:
                visited.append(element)
                print(element)
                for neighbor in self.graph[element]:
                    stack.append(neighbor)

    def dfs_recursive(self,v,visited):
        visited.append(v)
        print(v)
        for element in self.graph[v]:
            if element not in visited:
                self.dfs_recursive(element,visited)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Iterative Traversal")
g.dfs_iterative()
print("Recursive Traversal")
g.dfs_recursive(0,[])
