def countSteps(rem,ways):

    if rem == 0:
        return 1
    if rem < 0:
        return 0
    else:
        for i in range(1,4):
            ways += countSteps(rem-i,ways)
        return ways

print(countSteps(4,0))