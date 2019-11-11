def sortarray(arr):
    total_len = len(arr)
    if total_len == 0 or total_len == 1:
        return 0
    sorted_array = sorted(arr)
    ptr1 = 0
    ptr2 = 0
    counter = 0
    idx = 0
    while idx < total_len:
        if sorted_array[ptr1] == arr[ptr2]:
            ptr1 = ptr1 +1
            counter = counter + 1
        ptr2 = ptr2 + 1
        idx = idx +1

    return (total_len - counter)

print(sortarray([1,3,2]))