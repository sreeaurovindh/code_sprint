class Solution:
    def permute(self,nums:List[int] -> List[List[int]]):
        res = []
        def permuteHelper(start,end):
            if start == end:
                res.append(nums.copy())
            for i in range(start,end):
                nums[start],nums[i] = nums[i],nums[start]
                permuteHelper(start+1,end)
                nums[start],nums[i] = nums[i],nums[start]
        permuteHelper(0,len(n)-1)
        return res


t = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
t.sort(key=lambda x: (-x[0],x[1]))
