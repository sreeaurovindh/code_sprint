class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def printPathsUtil(curr_node, sum,
                   sum_so_far, path):

    # empty node
    if (not curr_node):
        return
    sum_so_far += curr_node.key

    # add current node to the path
    path.append(curr_node.key)

    # prthe required path
    if (sum_so_far == sum):

        print("Path found:", end=" ")
        for i in range(len(path)):
            print(path[i], end=" ")

        print()

        # if left child exists
    if (curr_node.left != None):
         printPathsUtil(curr_node.left, sum,
                       sum_so_far, path)

        # if right child exists
    if (curr_node.right != None):
         printPathsUtil(curr_node.right, sum,
                       sum_so_far, path)

        # Remove the current element
    # from the path
    path.pop(-1)


# A wrapper over printKPathUtil()
def printPaths(root, sum):
    path = []
    printPathsUtil(root, sum, 0, path)


if __name__ == '__main__':
    """ 10  
      /    \  
     28   13  
         /    \  
        14   15  
        / \  / \  
       21 22 23 24"""
    root = newNode(10)
    root.left = newNode(28)
    root.right = newNode(13)

    root.right.left = newNode(14)
    root.right.right = newNode(15)

    root.right.left.left = newNode(21)
    root.right.left.right = newNode(22)
    root.right.right.left = newNode(23)
    root.right.right.right = newNode(24)

    sum = 38
    printPaths(root, sum)