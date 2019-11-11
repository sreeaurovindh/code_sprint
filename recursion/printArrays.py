def recSum(arr):
    if len(arr) == 1:
        print(arr)
    else:
        new_inp = []
        for i in range(1,len(arr)):
            new_inp.append(arr[i-1]+arr[i])
        recSum(new_inp)
        print(arr)

recSum([1,2,3,4,5])
