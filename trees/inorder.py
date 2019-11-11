from collections import deque


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
        result.add(current.val);
        current = current.right

