def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for item in strs:
        while item.find(prefix) !=0:
            prefix = prefix[0:len(prefix)-1]
            if len(prefix) == 0:
                return ""
    return prefix

longestCommonPrefix(["flower","flow","flight"])