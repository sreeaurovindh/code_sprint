def find_conflicts(arr,row,col):
    num_ones = 0
    for i in range(len(arr)):
        if arr[row][i] == 1:
            num_ones += 1
    for i in range(1,len(arr)):
        if arr[i][col] == 1:
            num_ones += 1
    if num_ones > 1:
        return False
    return True


def valid_king(arr):
    for i in range(len(arr)):
        if not find_conflicts(arr,i,i):
            return False
    return True

valid_king([[1,0,0],[0,1,0],[0,0,1]])