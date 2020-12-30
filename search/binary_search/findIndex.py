def findRotatedIndexHelper(arr,item,lo,hi):
    if hi <= lo:
        return -1
    mid = (lo + hi)//2
    if arr[mid] == item:
        return mid
    elif item < arr[mid]:
        hi = mid -1
        return findRotatedIndexHelper(arr,item,lo,hi)
    else:
        lo = mid + 1
        return findRotatedIndexHelper(arr,item,lo,hi)

def findRotated(arr,item):
    lo = 0
    hi =  len(arr)
    return findRotatedIndexHelper(arr,item,lo,hi)

print(findRotated([6,7,8,9,10,1,2,3,4,5],3))
