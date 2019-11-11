def swap_zero(a):
    z_i= nz_i = 0
    for i in range(len(a)):
        if a[i] == 0:
            z_i = i
            if i+1 < len(a) and a[i+1] != 0:

                a[i],a[i+1]=a[i+1],a[i]
                z_i = i + 1
        else:
            nz_i = i
    return a
print(swap_zero([1,0,2,0,0,3,0,4,5,6]))
