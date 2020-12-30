# The problem assumes sorted order. But it does not throw
#  We did not check for these violations in the solution.

# The Recursive function below solves this problem and provides
# an efficient solution

##------------------------------------------------------------------##
#                       Iterative Routine                           #
##------------------------------------------------------------------##
def binary_search_single(arr,item):
    tot_len = len(arr) - 1
    if tot_len <= 0:
        return False

    left = 0
    right = tot_len

    if left == right and arr[left] != item:
        print("Item not found")

    while left < right and not found:

        if arr[left] > arr[right]:
            print("Array is not sorted")
            return -1

        mid = (left + right ) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
test_list_1 = [1,2,2,2,2,2,2,2,4]
print(binary_search_single(test_list_1, 2))
print(binary_search_single(test_list, 13))

##------------------------------------------------------------------##
#                       Recursive Routine                           #
##------------------------------------------------------------------##
def binary_search(arr,item):
    return binary_search(arr,item,lower,upper)

def binary_search(arr,item,lower,upper):
    # To check two conditions
    # If the two pointers have crossed each other.
    # In previous problem we do
    range = upper - lower
    if range < 0:
        print("Limits revered")
    # this means that there is only one item in the Array
    # and if that element is not the element we are looking for
    # then the item is not found.
    if range == 0 and arr[upper] != item:
        print("Item not found")

    if arr[lower] > arr[upper]:
        print("Array is not Sorted")

    center = (upper + lower) //2
    if(item == arr[center]):
        return center
    elif item < arr[center]:
        return binary_search(arr,item,lower,center-1)
    else:
        return binary_search(arr,item,center+1,upper)
##------------------------------------------------------------------##
