class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        i=0
        j=0
        running_sum = A[0]
        max_sum = A[0]
        for i in range(len(A)):
            running_sum += A[i]
            if running_sum > max_sum :
                max_sum = running_sum
            if(running_sum < 0):
                    running_sum = 0
        return max_sum
A= [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.maxSubArray(A))
