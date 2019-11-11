def moveY(input):
    if len(input) == 0:
        return input
    elif input[0]== "Y":
        return moveY(input[1:])+ "Y"
    else:
        return input[0] + moveY(input[1:])


print(moveY("YYYaYbYcY"))