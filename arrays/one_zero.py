def one_zero(a):
    '''
    This function moves all the zeros to the end of the array
    :param a:  The input array
    :return: Zeros arranged in the end
    '''
    last_char = a[0]
    z_i = None
    for i in range(len(a)):
        if a[i] == 0 and last_char == 0:
            continue
        elif a[i]!= 0:
            if z_i is not None:
                a[i],a[z_i] = a[z_i],a[i]
                # The next charecter will be swapped with next one.
                z_i = next_zero(a,z_i+1)
        elif a[i] == 0:
            z_i = i
        last_char = a[i]

    return a


def next_zero(a,start):
    '''
    This function find the index of the next zero charectear
    :param a: Inpurt array
    :param start:  the location from where to search
    :return:  The index is returned
    '''

    count = start
    for i in range(start,len(a)):
        if a[i] == 0:
            return count
        count = count + 1
    return None;

#Print the output of the funciton.
print(one_zero([1,0,2,0,0,3,0,9,4,5,6]))