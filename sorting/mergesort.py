# Merge sort

def sortElements(arr):
    mergesort(arr,[None] * len(arr),0,len(arr)-1)
    print(arr)
def mergesort(arr,temp,left,right):
    if left < right:
        mid = int((left + right) /2)
        mergesort(arr,temp,left,mid)
        mergesort(arr,temp,mid+1,right)
        merge(arr,temp,left,right)

def merge(arr,temp,leftStart,rightEnd):
    leftEnd  = int((leftStart+rightEnd)/2)
    rightStart = leftEnd+1
    
    left = leftStart
    right = rightStart
    index = left
    while left <= leftEnd and right <= rightEnd:
        if arr[left] <= arr[right]:
            temp[index]= arr[left]
            left = left + 1
        else:
            temp[index] = arr[right]
            right = right + 1
        index += 1
    
    if left <= leftEnd:
        temp[index:(leftEnd-left+1)] =  arr[left:leftEnd+1]
    
    if right <= rightEnd:
        temp[index:(rightEnd-right+1)] = arr[right:rightEnd+1]
    
    arr[leftStart:rightEnd+1] = temp[leftStart:rightEnd+1]

        

input = [4,6,1,2,5]
sortElements(input)