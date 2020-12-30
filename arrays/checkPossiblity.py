def checkPossibility(nums):
    if len(nums) < 1:
        return True
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1

    if count > 1:
        return False
    else:
        return True

print(checkPossibility([3,4,2,3]))