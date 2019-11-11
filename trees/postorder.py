from collections import deque


def post_order(root):
    result = []
    if root is None:
        return
    stack1 = deque([root])
    stack2 = deque()
    while len(stack1) > 0:
        root = stack1.pop()
        stack2.append(root)
        if root.left is not None:
            stack1.append(root.left)
        if root.right is not None:
            stack1.append(root.right)
    while len(stack2) > 0:
        root = stack2.pop()
        result.append(root)

    return result