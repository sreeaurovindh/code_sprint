def permuteHelper(s,chosen):
    if len(s) == 0:
        print(chosen)
    else:
        for i in range(len(s)):
            c = s[i]
            chosen = chosen+s[i]
            del s[i]

            permuteHelper(s,chosen)

            s.insert(i,c)
            del c[i]

permuteHelper("abc","")
