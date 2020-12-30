# BST

Title :
Date : Sep 25, 2020 8:22:13 PM
Tags: #BST #Trees
External Link: 
1. https://medium.com/leetcode-patterns/leetcode-pattern-0-iterative-traversals-on-trees-d373568eb0ec





## Qn: Validate if Tree is a BST

For a binary tree to be a BST the inorder has to be in **sorted(ascending)** order

>  So the question boils down to How do we check if the value is 

![](../../Trees/vlidbst_2020-09-25-20-46-18.png)

```python
def validBSTTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        stack = deque([])
        current  = root
        # result = []
        prev = None
        while len(stack) != 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None and prev.val >= current.val:
                return False
            prev = current
            # result.append(current.val);
            current = current.right
        return True

```

[[DFS]]