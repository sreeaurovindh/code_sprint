G = {'A': set(['B', 'C']),
     'B': set(['A', 'D', 'E']),
     'C': set(['A', 'F']),
     'D': set(['B']),
     'E': set(['B', 'F']),
     'F': set(['C', 'E'])}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    ##    if not graph.has_key(start):
    ##        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


print(find_path(G, 'A', 'F'))
