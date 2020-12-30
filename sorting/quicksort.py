def sort_array(inp):
    quicksort(inp,0,len(inp)-1)
    print(inp)


def quicksort(inp,left,right):
    if left < right: # Strictly less than left
        pivot_index = int((left+right)/2)
        pivot = inp[pivot_index]
        index = partition(inp,left,right,pivot)
        quicksort(inp,left,index-1)
        quicksort(inp,index,right)


def partition(inp,left,right,pivot):
    while left <= right:
        while inp[left] < pivot:
            left += 1
        while inp[right] > pivot:
            right -= 1
        if left <= right:
            inp[left], inp[right] = inp[right], inp[left]
            left += 1
            right -= 1
    return left

sort_array([5,3,4,1,2])