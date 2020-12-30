def diehelper(dice,chosen,indent,i):
    #print(indent,"diehelper(",dice,chosen,i,")")
    if dice == 0:
        print(chosen)
    else:
        for i in range(1,7):
            chosen.append(i)

            diehelper(dice-1,chosen,indent+"  ",i)

            del chosen[-1]
            #print(indent+"deleting last")


diehelper(3,[],"",-1)
