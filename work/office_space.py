import sys
from collections import deque

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

x_direction = [1,-1,0,0]
y_direction = [0,0,-1,1]

def findMinDist(n,w,h):
    grid = [[-1 for i in range(h)] for j in range(w)]
    return solve(n,w,h,0,0,grid)

def solve(remaining,w,h,row,col,grid):
    if remaining == 0:
        return searchbfs(w,h,grid)
    r = row
    c = col
    if col < h:
        r = r + int(col/h)
        c =  int(col%h)

    min_distance = sys.maxsize
    for i in range(r,w):
        for j in range(c,h):
            grid[i][j] = 0
            value = solve(remaining-1,w,h,i,j+1,grid)
            min_distance = min(min_distance,value)
            grid[i][j] = -1
    return min_distance

def searchbfs(w,h,grid):
    dist = []
    for i in range(w):
        temp = []
        for j in range(h):
            temp.append(grid[i][j])
        dist.append(temp)

    queue = deque([])
    max_dist = 0
    for i in range(0,w):
        for j in range(0,h):
            if dist[i][j] == 0:
                queue.append(Point(i,j))

    while len(queue)!= 0:
        item = queue.popleft()
        x_val = item.x
        y_val = item.y
        max_dist = max(max_dist,dist[x_val][y_val])

        for i in range(4):
            x_new = x_val + x_direction[i]
            y_new = y_val + y_direction[i]

            if x_new >= w or y_new >= h or x_new < 0 or y_new < 0:
                continue
            if dist[x_new][y_new] == -1:
                dist[x_new][y_new] = dist[x_val][y_val] + 1
                queue.append(Point(x_new,y_new))

    return max_dist

print(findMinDist(2,2,3))