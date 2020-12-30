# simple exponentail function
def exponential(a,n):
    if n==0:
        return 1
    else:
        return a*exponential(a,n-1)
    
print(exponential(5,5))