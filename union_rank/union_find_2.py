def find(value,root):
    while value!=root[value]:
        value = root[value]
    return value

def union(val1,val2,root,rank):
    val1_root = find(val1,root)
    val2_root = find(val2,root)

    if val1_root == val2_root:
        return

    if rank[val1_root] < rank[val2_root]:
        root[val1_root] = root[val2_root]
        rank[val2_root] += rank[val1_root]
    else:
        root[val2_root] = root[val1_root]
        rank[val1_root] += rank[val2_root]


def connectedCities(n,g,originCities,destinationCities):
    root = [0] * (n+1)
    rank = [0] * (n+1)
    result = []
    for i in range(n+1):
        root[i] = i
        rank[i] = 1


    for i in range(g+1,n+1):
        for j in range(2*i,n+1,i):
            print(i,j)
            union(i,j,root,rank)

    for i in range(len(originCities)):
        if find(originCities[i],root) == find(destinationCities[i],root):
            result.append(1)
        else:
            result.append(0)

    return result

print(connectedCities(6,1,[1,2,4,6],[3,3,3,4]))
