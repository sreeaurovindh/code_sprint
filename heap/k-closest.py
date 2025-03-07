import heapq
class Solution:
    def kClosest(self, points, k: int):
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

s=Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]],2))