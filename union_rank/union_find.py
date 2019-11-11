import math
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

# A utility function to find set of an element


# node(uses path compression technique)
def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


# A function that does union of two sets
# of u and v(uses union by rank)
def union(subsets, u, v):
    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v

        # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


def get_factors(n,threshold):
    results = set()
    flag = False
    for i in range(int(math.sqrt(n)) + 1,0,-1):
        if n % i == 0:
            remainder = int(n/i)
            if remainder > threshold and i > threshold:
                results.add(max(remainder,i))
                results.add(min(remainder, i))
                flag = True
            elif remainder > threshold:
                results.add(remainder)
                flag = True
            elif i > threshold:
                results.add(i)
                flag = True

    return (flag,results)


def has_common_gcd(origin_gcd,destn_gcd):
    o_gcd_len = len(origin_gcd)
    d_gcd_len = len(destn_gcd)
    origin_gcd = list(origin_gcd)
    destn_gcd = list(destn_gcd)
    if o_gcd_len == 0 or d_gcd_len == 0:
        return False
    i = j = 0
    while i < len(origin_gcd) and j < len(destn_gcd):
        if origin_gcd[i] == destn_gcd[j]:
            return True
        elif origin_gcd[i] > destn_gcd[j]:
            j+=1
        else:
            i+=1
    return False


def connectedCities(n,g,originCities,destinationCities):
    subsets = [Subset(0, 0)]
    origin_flags = []
    destn_flags = []
    output = [0]*(len(originCities))
    one_origin_city_found = False
    one_destn_city_found = False

    for item in originCities:
        subsets.append(Subset(item, 0))
        flag,common_factors = get_factors(item,g)
        if flag:
            one_origin_city_found = True
            origin_flags.append((flag,common_factors,item))


    for item in destinationCities:
        subsets.append(Subset(item, 0))
        flag,common_factors = get_factors(item,g)
        if flag:
            one_destn_city_found = True
            destn_flags.append((flag,common_factors,item))

    if not one_origin_city_found or not one_destn_city_found:
        return output

    all_items = origin_flags + destn_flags

    for idx1,origin_item in enumerate(all_items):
        for idx2,destn_item in enumerate(all_items):
            if idx1 != idx2:
                if has_common_gcd(origin_item[1], destn_item[1]):
                    union(subsets, origin_item[2] , destn_item[2])


    for i in range(len(originCities)):
        if find(subsets,originCities[i]) == find(subsets,destinationCities[i]):
            output[i] = 1
        else:
            output[i] = 0

    return output








print(connectedCities(6,1,[1,2,3],[4,5,6]))
