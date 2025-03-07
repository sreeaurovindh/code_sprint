from collections import defaultdict

def connected_components(n,edge_list):
    # The setup
    # Initialization with list
    adj_list = defaultdict(list)
    
    # Populate the adj list with edge info
    for i in range(len(edge_list)):
        # If undirected we add both sides
        adj_list[edge_list[i][0]].append(edge_list[i][1])
        adj_list[edge_list[i][1]].append(edge_list[i][0])
    
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if visited[i] == False:
            count = count + 1
            dfs_helper(adj_list,i,visited)
    
    return count
            
def dfs_helper(adj_list, index,visited):
    visited[index] = True
    for i in adj_list[index]:
        if visited[index] == False:
            dfs_helper(adj_list,i,visited)
    

    

connected_components()