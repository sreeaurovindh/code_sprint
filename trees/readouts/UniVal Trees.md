# Unival Trees

```python
class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.inorder(root,val=None)
        
    def inorder(self,root,val):
        if root is None:
            return None
        if val is None:
            val = root.val
        elif val != root.val:
            return False
            
        left_val = self.inorder(root.left,val)
        right_val = self.inorder(root.right,val)
        
        if left_val is False or right_val is False:
            return False
        else:
            return True
        
```

