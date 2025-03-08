# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # This variable will store the maximum diameter found during traversal.
        self.max_diameter = 0

        def depth(node: TreeNode) -> int:
            # Base case: if the node is None, return a height of 0.
            if not node:
                return 0
            
            # Recursively compute the depth (height) of the left subtree.
            left_depth = depth(node.left)
            # Recursively compute the depth (height) of the right subtree.
            right_depth = depth(node.right)
            
            # The diameter through this node is the sum of the left and right depths.
            # This represents the longest path that passes through the current node.
            current_diameter = left_depth + right_depth
            
            # Update the global maximum diameter if the current one is larger.
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of the current node.
            # Height is max depth of its subtrees plus one for the current node.
            return max(left_depth, right_depth) + 1

        # Start the depth-first search from the root.
        depth(root)
        # After the DFS, self.max_diameter contains the diameter of the tree.
        return self.max_diameter

 
 # Example Usage:
# Construct a simple binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
if __name__ == "__main__":
    # Create nodes
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    # Create an instance of the solution and compute the diameter.
    sol = Solution()
    print("Diameter of the binary tree is:", sol.diameterOfBinaryTree(root))