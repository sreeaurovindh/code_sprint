from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode

class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return None
        stack = deque([root])
        current  = None
        result = []
        while len(stack) != 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val);
            current = current.right
        return result
    
t = Solution()
lst_inp = [1,None,2,3]
root = creatBTree(lst_inp,0)
print(t.inorderTraversal(root))

