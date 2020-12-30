def func(i):
    if i % 2 == 0:
        i = i+1
        return i
    else:
        x = func(i-1)
        print('Value of X is ',x)
        return func(x)


func(399)