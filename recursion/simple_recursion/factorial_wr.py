# Problem Statement:
# To compute factorial of n storing results at each stage using recursion
# For ex: results[1] = 1, results[2]= 2 results[3] = 6



def allFactorials(n):
    results = []
    doAllFactorials(n,results,0)
    return results

def doAllFactorials(n,results,level):
    if n >  1:
        # Important!
        # In recursion, The answer to all problems are calculated at a reverse manner
        # Imagine stack! :)
        #  N ranges from N to zero while level ranges from 0 to N. Also we have
        # to calculate store the results at each level .

        results[level] = n * doAllFactorials(n-1,results,level + 1)
        return results[level]
    else:
        results[level] = 1
        return 1

def open_file():
    with open("D:/dv/yelp_ds") as myfile:
        head = [next(myfile) for x in range(12)]
    print(head)
    

open_file()