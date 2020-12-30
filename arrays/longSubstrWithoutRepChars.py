## To find a substring based on specified charecteristic
## The Two pointer concept works better ALWAYS!!



##def lengthOfLongestSubstring(s):
##    """
##    :type s: str
##    :rtype: int
##    """

##    tot_len = len(s)
##    if tot_len == 1:
##        return 1

##    repeated_char = {}
##    max_char_count = 0
##    current_count = 0
##    last_char = ''
##    for symbol in s:
##        if symbol in repeated_char or symbol == last_char:
##            last_char = symbol
##            current_count = 1
##            del repeated_char[symbol]
##        else:
##            current_count = current_count + 1
##            repeated_char[symbol] = 1
##        if max_char_count < current_count:
##            max_char_count = current_count
##    return max_char_count

def lengthOfLongestSubstring(s):
    n = len(s)
    repeats = set()
    ans = i = j = 0
    while i < n and j < n :
        if s[j] not in repeats:
            repeats.add(s[j])
            j = j + 1
            ans = max(ans,j - i)
        else:
            repeats.remove(s[i])
            i = i + 1
    return ans

print(lengthOfLongestSubstring("auro")) #4
print(lengthOfLongestSubstring("auro")) #4
print(lengthOfLongestSubstring("auroaaa")) #4
print(lengthOfLongestSubstring("abcabcdefa")) # 6
print(lengthOfLongestSubstring("auroauroaurovi")) #6
print(lengthOfLongestSubstring("")) #0
print(lengthOfLongestSubstring("a")) #1
print(lengthOfLongestSubstring("eee")) #1
print(lengthOfLongestSubstring("dvdf")) #3
