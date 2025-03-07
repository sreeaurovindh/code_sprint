graph = {'A': set(['B', 'C']),
         'B': set(['D', 'E']),
         'C': set(['F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_iter(graph,node):
    visited = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([x for x in graph[node] if x not in visited])


def matrix_transpose():
    m = [[1, 2], [3, 4], [5, 6]]


    for row in m:
        print(row)
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    for row in rez:
        print(row)

dfs_iter(graph)


def run_dfs(self,v):
    visited = [False] * len(self.graph)
    self.dfs_util(v,visited)
    
def dfs_util(self,v,visited):
    visited[v] = True
    print(v)
    
    for i in self.graph[v]:
        if visited[i] == False:
            self.dfs_util(self.v,visited)