def recurse(a,i):
    if i == len(a)-1:
        print(a[i])
        return
    else:
        recurse(a,i+1)
        print(a[i])


recurse([1,2,3,4,5],0)