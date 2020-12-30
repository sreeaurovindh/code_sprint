def findRotatedIndexHelper(arr,item,lo,hi):
    if hi <= lo:
        return -1
    mid = (lo + hi)//2


def findRotated(arr,item):
    lo = 0
    hi =  len(arr)
    return findRotatedIndexHelper(arr,item,lo,hi)

print(findRotated([6,7,8,9,10,1,2,3,4,5],3))
