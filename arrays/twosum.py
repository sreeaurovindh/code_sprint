
# Time Complexity = O(n), Space Complexity O(1)
def two_sum(arr):
    result = []
    arr.sort()
    j = 0
    k = len(nums) - 1
    while j<k:
        if nums[i] + nums[j] +nums[k] == 0:
            result.append([nums[j],nums[k]])
            while j<k and nums[j]==nums[j+1]:
                j+=1
            while j<k and nums[k] == nums[k+1]:
                k-=1
            j+=1
            k-=1
        elif nums[i] +nums[j] + nums[k] > 0:
            k-=1
        else:
            j+=1
    return result


# Time Complexity = O(n), Space Complexity O(n)
def two_sum(nums,target):
    store = {}
    for i in range(len(nums)):
        if nums[i] in store:
            return [i,store[nums[i]]]
        else:
            store[target-nums[i]] = i
    return []
