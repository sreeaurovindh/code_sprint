class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cell_perimeter = 4
                    if r-1 >=0 and grid[r-1][c] == 1:
                        cell_perimeter -=1 
                    if r+1 <= rows - 1 and grid [r+1][c] == 1:
                        cell_perimeter -=1 
                    if c-1  >= 0 and grid[r][c-1] ==1 :
                        cell_perimeter-= 1
                    if c+1 <= cols - 1 and grid[r][c+1] == 1:
                        cell_perimeter -=1 
                    perimeter += cell_perimeter
        return perimeter
    