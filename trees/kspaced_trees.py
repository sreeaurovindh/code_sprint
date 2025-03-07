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
    def distanceK(self, root , target , k):
        parentDict={}
        def dfs(current,parent):
            parentDict[current]=parent
            if current.left:
                dfs(current.left,current)
            if current.right:
                dfs(current.right,current)
        dfs(root,None)
        
        q=deque([(target,0)])
        isVisited={target}
        
        while q:
            node,dist=q.popleft()
            if dist==k:
                return [node.val]+ [node.val for node, d in q]
            for node1 in (node.left,node.right,parentDict[node]):
                if node1 and node1 not in isVisited:
                    isVisited.add(node1)
                    q.append((node1,dist+1))
        return []-

t = Solution()
lst_inp = [3,5,1,6,2,0,8,None,None,7,4]
root = creatBTree(lst_inp,0)
t.distanceK(root,TreeNode(5),2)