from collections import deque
import sys
input = [6,2,4]
stack = deque([])
ans = 0
for i in range(len(input)):
    if i == len(input):
        current_value = sys.maxsize
    else:
        current_value = input[i]

    while (len(stack)!=0) and (current_value >= stack[-1]):
        value = stack.pop()
        if len(stack) == 0:
            if current_value == sys.maxsize:
                ans += 0
            else:
                ans += current_value * value
        else:
            ans += (value * min(stack[-1],current_value))
    stack.append(current_value)
print(ans)