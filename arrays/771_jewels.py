
class Solution:
    def subarrayBitwiseORs(self, A):
        
        
        res = set()
 
        pre = {0}
 
        for x in A:
            pre = {x | y for y in pre} | {x}
            res |= pre
    
        return len(res)
    

    
s = Solution()
s.subarrayBitwiseORs([3,4,5])
