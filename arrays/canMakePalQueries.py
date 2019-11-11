def canMakePaliQueries(s, queries):
    """
    :type s: str
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    ans = []
    for query in queries:
        inp_str = s[query[0]:(query[1] + 1)]
        inp_dict = {}
        for letter in inp_str:
            if letter not in inp_dict:
                inp_dict[letter] = 1
            else:
                inp_dict[letter] = inp_dict[letter] + 1
        total_no_pairs = 0
        for values in inp_dict.values():
            if values % 2 != 0:
                total_no_pairs += 1
        if len(inp_str) == 1:
            ans.append(True)
        elif len(inp_str) %2 == 0:
            if (total_no_pairs - query[2]) <= 0 or (total_no_pairs - (2*query[2]) <= 0):
                ans.append(True)
            else:
                ans.append(False)
        else:
            if (total_no_pairs -1 - query[2]) <= 0 or (total_no_pairs -1 - (2*query[2]) <= 0):
                ans.append(True)

            else:
                ans.append(False)
    return ans


s = "orsrurgtinans"
query = [[6,12,3]]
print(canMakePaliQueries(s,query))



