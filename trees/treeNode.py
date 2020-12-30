class treeNode:
    
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

    def set_left(self,value):
        self.left = value

    def set_right(self,value):
        self.right = value

    def buildTree(self):
        root = Node(20)
        root.left = Node(8)
        root.left.left = Node(4)
        root.left.right = Node(12)
        root.left.right.left =  Node(10)
        root.left.right.right = Node(14)
        root.right = Node(22)
        root.right.right = Node(25)
        return root

