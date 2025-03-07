from collections import defaultdict, deque
class Graph:
    # Graph Traversal using Depth first Search
    def __init__(self,num_nodes):
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs_iterative(self):
        stack = [1]
        visited = []
        result = []
        while stack:
            element = stack.pop()
            if element not in visited:
                visited.append(element)
                result.append(element)
                for neighbor in self.graph[element]:
                    stack.append(neighbor)
        return result

    def dfs_recursive(self,v,visited,result):
        visited.append(v)
        result.append(v)
        for element in self.graph[v]:
            if element not in visited:
                self.dfs_recursive(element,visited,result)
                
        return result
                
    def bfs_iterative(self,root):
        queue = deque()
        visited = [False] * (self.num_nodes + 1)
        if root:
            queue.append(root)
            # we mark as visited only after we append it to the queue
            visited[root]= True
        
        level = 0
        result = []
        while len(queue) > 0:
            curr = queue.popleft()
            result.append(curr)
            
            for i in self.graph[curr]:
                if not visited[i]: 
                    queue.append(i)
                    visited[i] = True
        level +=1
             
        
        return result,level
                
        
        


g = Graph(4)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(3, 4)
g.addEdge(4, 4)

print("Iterative Traversal DFS")
result = g.dfs_iterative()
print(result)

print("Recursive Traversal DFS")
result = g.dfs_recursive(1,[],[])
print(result)


print("Recursive Traversal BFS")
result,level = g.bfs_iterative(1)
print(result,level)
