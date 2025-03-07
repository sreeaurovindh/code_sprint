# https://yunrui-li.medium.com/leetcode-union-find-data-sturcture-96ceb52eafe7
import collections
from typing import List
class UnionFindSet:
    def __init__(self, n):
        self._parents = [node for node in range(n)]
        self._ranks = [1 for _ in range(n)]
        
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return False
    
class Solution:
    """
    Thought Process:
        Apparently, we can treat thsi matrix as an undirected graph.
            1.each cell(i, j) represents a certain node in graph, Totally, m*n nodes.
            2.there's edge going to left, right, up, and down for each cell. 
            Totally, 4 directions.
            3. Given grid, intrinsically, it's a adjacency matrix data structure.
            
        DFS:
        Atually, this problem can come downs to number of connected component in the graph.
            step1: we traverse each cell
                For each step, if it's not visited yet, we do dfs on grip.
            step2: number of times we do dfs is equal to nb_landss
        
        Union-Find
            step1: we traverse each cell
                For each step, 
                    if cell is water, we do nothing.
                    else:
                        do union method provided by union-find data sturcture with neighbor node if neighbor node is also 1(land)
            step2: we iterge all nodes.
                For each node, we get root node of this current node using find method provided by Union-Find data structure. At the same time, we use hashmap or hashset to store nb of root node for each cell.
            step3: number of uniue parent node we have is equal to nb of connected components we in this graph
                
    Note:
        When we use union-find, each node represetns from 0 to n
    For example,
        0, 1, 2, 3, 4, 5 (n)
      0 0  1  2  3  4  5
      1 6  7  8  9  10 11
      2 12 13 14 15 16 17
      3 18 19 20 21 22 23
     (m)
     totally, 4*6=24 nodes
     For each cell, the index formula is 
        i * n + j
        For example, 
            first row(i==0), j = 0 to 5
            second row(i==1), 1*6+j, where j = 0 to 5
    Reference:
        https://leetcode.com/problems/number-of-islands/discuss/464655/Python-Union-Find-Commented-Clean-and-Easy
        
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        T:O(m*n)
        S:O(m*n) because we use visited set and recursion stack from dfs might go m*n step deeped in case every grid is land.
        """
        m = len(grid)
        n =len(grid[0])
        
        self.m = m
        self.n = n
        visited = set([])
        nb_lands = 0
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    self.dfs(i, j, visited, grid)
                    nb_lands+=1
        return nb_lands
            
    def dfs(self, x, y, visited, graph):
        if graph[x][y] == "0":
            return
        visited.add((x,y))
        for direction in self.directions:
            x_next, y_next = x+direction[0], y+direction[1]
            if (x_next, y_next) in visited:
                continue 
            if 0<=x_next < self.m and 0<=y_next< self.n:
                self.dfs(x_next, y_next, visited, graph)
                
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Union-Find
        S:O(n*m) because we use union-find data sturcture.
        """
        m = len(grid)
        n =len(grid[0])
        
        self.m = m
        self.n = n
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        unionfind = UnionFindSet(m*n)
        # step1: takes O(n*m)
        for i in range(m):
            for j in range(n):
                # there's no path to water
                if grid[i][j] == "0":
                    continue
                # there's path to neighbor land
                for direction in self.directions:
                    x_next, y_next = i+direction[0], j+direction[1] 
                    if 0<=x_next < self.m and 0<=y_next< self.n and grid[x_next][y_next] == "1":
                        cur_node_idx = i*n+j
                        nei_node_idx = x_next*n+ y_next
                        unionfind.union(cur_node_idx, nei_node_idx)
        # step2: takes O(n*m) in worst case that every cell is land
        # find unique number of root node
        count = collections.defaultdict(int) # with this count, we can also know number of lands in each component.
        for i in range(m):
            for j in range(n):
                # there's no path to water
                if grid[i][j] == "0":
                    continue
                cur_node_idx = i*n+j # land
                root_node = unionfind.find(cur_node_idx)
                count[root_node] += 1
