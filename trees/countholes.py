
def countHoles(number):
    total = 0
    while number > 0:
        digit = number %10
        print(digit)
        if digit  == 1 or digit == 2 or digit ==3 or digit == 5 or digit == 7:
            total = total + 0
        elif digit  == 0 or digit == 4 or digit ==6 or digit == 9 :
            total = total + 1
        elif digit == 8:
            total = total + 2

        number = number / 10

    return total


countHoles(1288)