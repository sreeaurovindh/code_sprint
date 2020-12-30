import math
def convert_to_int(input):
    input_len = len(input)
    sum = int(input[input_len-1])
    for i in range(1,input_len):
        value = math.pow(10,i) * int(input[input_len-i-1])
        sum += value
    return int(sum)


print(convert_to_int('123456'))