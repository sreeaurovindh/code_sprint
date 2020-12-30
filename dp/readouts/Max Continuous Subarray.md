# Maximum Continuous Sub Array - Kadane Algorithm

```Python
def maxSubArray(self, nums):
      """
      This function finds the maxiumum sum of subarray.
      It is the Kadane's Algorithm
      It uses current_max and global Max to keep track of the maximum sum of elements.
      :type nums: List[int]
      :rtype: int
      """
      global_max = nums[0]
      current_max = nums[0]
      for i in range(1,len(nums)):
      		if current_max <0:
      				current_max = nums[i]
      		else:
      				current_max = current_max +  nums[i]
      		if current_max > global_max:
      				global_max = current_max

      return global_max

```

