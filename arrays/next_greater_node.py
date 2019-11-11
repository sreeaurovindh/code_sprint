

def next_largest_element(input):
    result = [0] * (len(input))
    last_max_element = input[len(input)-1]

    for i in range(len(input)-1,-1,-1):
        print(input[i],last_max_element)
        if input[i] < last_max_element:
            result[i] = last_max_element
        else:
            result[i] = 0
            last_max_element = input[i]
    print(result)





input = [1,7,5,1,9,2,5,1]
next_largest_element(input)
