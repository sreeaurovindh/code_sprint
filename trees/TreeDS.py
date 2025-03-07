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
    def postorderTraversal(self, root):
        result = []
        if root is None:
            return result
        stack = []
        stack.append(root)
        while len(stack) > 0 :
            curr = stack.pop()
            result.append(curr.val)
            if curr.left is not None:
                stack.append(root.left)
            if curr.right is not None:
                stack.append(root.right)
        return list

t = Solution()
lst_inp = [3,5,1,6,2,0,8,None,None,7,4]
root = creatBTree(lst_inp,0)
t.distanceK(root,TreeNode(5),2)