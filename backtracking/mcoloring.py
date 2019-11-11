# List of colors = col = [0,1,2,3]
# List of Nodes = [1,2,3,4,5]
# List of choices = [0,1,0,2,0]
# adjacency_matrix = adj_m N*N

def valid_configuration(choices, adj_m):
    total_choices = len(choices)
    for i in range(len(choices)):
        for j in range(len(adj_m[0])):
            if j < total_choices:
                if adj_m[i][j] == 1 and choices[j] == choices[i]:
                    return False
            else:
                break
    return True


def mcoloring(choices, colors, adj_m):
    if len(choices) == len(adj_m):
        print(choices)
        return True
    else:
        for i in colors:
            choices.append(i)
            if valid_configuration(choices, adj_m):
                output = mcoloring(choices, colors, adj_m)
                if output is True:
                    return True
            choices.pop()
    return False


adj_m=[[0,0,1,1,0],[0,0,0,1,1],[1,0,0,0,1],[1,1,0,0,0],[0,1,1,0,0]]
choices = []
colors = [0,1,2,3]
mcoloring(choices,colors,adj_m)