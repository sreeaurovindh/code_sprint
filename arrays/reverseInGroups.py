def reverse_in_grps(arr,k):
    if k == 1:
        return

    tot_len = len(arr) -1

    for i in range(0,tot_len,k):
        j = min(tot_len,i+k-1)
        while i < j:
            swap(arr,i,j)
            i = i +1
            j = j - 1




def swap(arr,ind1,ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


a=[i for i in range(1,50)]
b= [1,2,3,4,5]

reverse_in_grps(a,10)
print(a)
reverse_in_grps(b,3)
print(b)
