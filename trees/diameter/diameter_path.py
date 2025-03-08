# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Global variables to track maximum diameter (in edges) and its path.
        self.max_diameter = 0
        self.max_path = []

        def dfs(node: TreeNode):
            """
            Returns a tuple:
              (height, path)
            where:
              - height: the maximum number of edges from this node down to a leaf.
              - path: list of nodes from the current node down along that longest path.
            For a leaf node, height is 0 and path is [node].
            """
            if not node:
                # For an empty subtree, we return height = -1 and empty path.
                # (Height = -1 makes the math work out: a leaf will have height -1+1 = 0.)
                return -1, []
            
            left_height, left_path = dfs(node.left)
            right_height, right_path = dfs(node.right)
            
            # Determine the best downward path starting at the current node.
            if left_height >= right_height:
                best_down = [node] + left_path
                best_height = left_height + 1
            else:
                best_down = [node] + right_path
                best_height = right_height + 1

            # Now, consider the candidate diameter path that goes through this node.
            # If both children exist, the candidate path is:
            # (left path from leaf to node) + (node) + (right path from node to leaf)
            if node.left is not None and node.right is not None:
                candidate_length = left_height + right_height + 2  # number of edges
                candidate_path = left_path[::-1] + [node] + right_path
            else:
                # If only one child exists (or none), the candidate is the best downward path.
                # (For a leaf, best_height is 0, which is the correct diameter.)
                candidate_length = best_height
                candidate_path = best_down

            # Update global maximum diameter if this candidate is larger.
            if candidate_length > self.max_diameter:
                self.max_diameter = candidate_length
                self.max_path = candidate_path

            return best_height, best_down

        dfs(root)
        return self.max_diameter

    def getDiameterPath(self, root: TreeNode):
        """
        Computes the diameter (and sets self.max_path).
        Then returns the path (list of node values) of the diameter.
        """
        self.diameterOfBinaryTree(root)  # This updates self.max_path.
        # Convert nodes to their values for easy printing.
        return [node.val for node in self.max_path]

# Example Usage:
# Construct the following binary tree:
#
#         1
#        / \
#       2   3
#      / \
#     4   5
#
# The diameter is the path [4, 2, 1, 3] with 3 edges.

if __name__ == "__main__":
    # Create nodes
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root = TreeNode(1, node2, node3)

    sol = Solution()
    diameter_length = sol.diameterOfBinaryTree(root)
    diameter_path = sol.getDiameterPath(root)

    print("Diameter length (number of edges):", diameter_length)
    print("Path of the diameter (node values):", diameter_path)
