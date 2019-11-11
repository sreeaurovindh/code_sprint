# Python3 program to find the numbers
# of non negative integral solutions

# return number of non negative
# integral solutions
def countSolutions(n, val,indent):
    print(indent+"countSolutions(",n,val,")")
    # initialize total = 0
    total = 0

    # Base Case if n = 1 and val >= 0
    # then it should return 1
    if n == 1 and val >= 0:
        return 1

    # iterate the loop till equal the val
    for i in range(val + 1):
        # total solution of of equations
        # and again call the recursive
        # function Solutions(variable,value)
        total += countSolutions(n - 1, val - i,indent+"  ")

    # return the total no possible solution
    return total


# driver code
n = 4
val = 2
print(countSolutions(n, val,""))