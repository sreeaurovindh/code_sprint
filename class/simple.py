def recursive_exponential(a,n):
    if n == 0:
        return 1
    else:
        return a * recursive_exponential(a,n-1)
    
print(recursive_exponential(2,4))