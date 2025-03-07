def numIslands(self, grid):
    islands = 0

    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "1":
                islands += 1
                self.dfs(grid, i, j)
    return islands


def dfs(self, grid, r, c):
    nr1 = len(grid)
    nc1 = len(grid[0])
    grid[r][c] = "0"
    if (r - 1) >= 0 and grid[r - 1][c] == "1":
        self.dfs(grid, r - 1, c)
    if (r + 1) < nr1 and grid[r + 1][c] == "1":
        self.dfs(grid, r + 1, c)
    if (c - 1) >= 0 and grid[r][c - 1] == "1":
        self.dfs(grid, r, c - 1)
    if (c + 1) < nc1 and grid[r][c + 1] == "1":
        self.dfs(grid, r, c + 1)
