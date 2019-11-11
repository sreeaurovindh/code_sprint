#https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/369191/JavaScript-with-Explanation-no-substring-comparison-fast-O(n)-time-O(1)-space.-(Credit-to-nate17)
def lastSubstring(input):
    start = end = 0
    skip = 1

    while (skip+end) < len(input):
        if input[start+end] == input[skip+end]:
            end += 1
        elif input[start+end] < input[skip+end]:
            start = max(start+end+1,skip)
            skip = start+1
            end= 0
        elif input[start+end] > input[skip+end]:
            skip = skip+end+1
            end=0

    return input[start:]

print(lastSubstring('zyxbzyxc'))