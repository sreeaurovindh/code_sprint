def fmax(arr,mVal,n):
    if n == len(arr):
        return mVal
    else:
        if mVal <arr[n]:
            mVal = arr[n]
        return fmax(arr,mVal,n+1)

a = [3,4,1,55,66,2]
print(fmax(a,a[0],0))