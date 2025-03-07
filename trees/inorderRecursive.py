
def inorder(root,result):
    if not root:
        return
    result.append(root.data)
    inorder(root.left,result)
    inorder(root.right,result)


inorder(None,[])
