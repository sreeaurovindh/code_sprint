from collections import deque
from typing import List
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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        def helper(node, isroot):
            if not node:
                return 
           
            nodeDel = node.val in to_delete
            if isroot and not nodeDel:
                res.append(node)
                
            node.left = helper(node.left,nodeDel)
            node.right = helper(node.right, nodeDel)
            return None if nodeDel else node
        
        helper(root, True)
        # print(len(res))
        return res
        
        
t = Solution()
lst_inp = [1,2,3,4,5,6,7]
to_delete = [3,5]
root = creatBTree(lst_inp,0)
t.delNodes(root,to_delete)