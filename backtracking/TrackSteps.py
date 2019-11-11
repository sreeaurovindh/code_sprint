def trackSteps(n,path):
    if n==0:
        print(path)
    else:
        for i in range(1,4):
            path.append(i)
            if n-i >= 0:
                trackSteps(n-i,path)
            path.pop()

trackSteps(6,[])