def dfs(graph, current, goal, path=None, visited=None):
    # Initialize path and visited set on the first call
    if path is None:
        path = [current]
    if visited is None:
        visited = set([current])
    
    # If we reached the goal, return the current path
    if current == goal:
        return path
    
    # Traverse the neighbors of the current node
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            # Add the neighbor to the visited set and extend the current path
            visited.add(neighbor)
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result
    # If no path is found from this branch, return None
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'
path_found = dfs(graph, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", path_found)
