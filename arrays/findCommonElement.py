def find_common_element(a, b, c):
    i = j = k = 0
    a_len = len(a) - 1
    b_len = len(b) - 1
    c_len = len(c) - 1
    while i <= a_len and j <= b_len and k <= c_len:
        max_element = max([a[i], b[j], c[k]])
        while i < a_len and a[i] < max_element:
            i += 1
        while j < b_len and b[j] < max_element:
            j += 1
        while k < c_len and c[k] < max_element:
            k += 1
        if a[i] == b[j] == c[k]:
            return a[i]
    return None


print(find_common_element([1, 2, 3, 4, 6,8], [6, 7,8, 9], [1,2,3,8]))
print(find_common_element([1, 2, 3, 4, 6,8], [6, 7,8, 9], [8]))
print(find_common_element([1, 2, 3, 4, 7 ,8], [6, 7,8, 9], [6,7]))