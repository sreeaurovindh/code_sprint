# Tree Traversal Examples

Interview: No
Status: Revise
Type: Trees

# Trees

“Top-down” means that in each recursive call, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the “top-down” solution can be considered as a kind of **preorder**traversal.

To be specific, the recursive function top_down(root, params) works like this:

```python
return specific value for null node
update the answer if needed   // answer <-- params
left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params 
return the answer if needed                      // answer <-- left_ans, right_ans

```

## Maximum Depth Problem

We know that the depth of the root node is 1. For each node, if we know its depth, we will know the depth of its children. Therefore, if we pass the depth of the node as a parameter when calling the function recursively, all the nodes will know their depth. And for leaf nodes, we can use the depth to update the final answer

```python
return if root is null
if root is a leaf node:
    answer = max(answer, depth)         // update the answer if needed
maximum_depth(root.left, depth + 1)      // call the function recursively for left child
maximum_depth(root.right, depth + 1)     // call the function recursively for right child

```

#Coding-Interview/Trees/Recursive/top-down

## Bottom up Traversal

“Bottom-up” is another recursive solution. In each recursive call, we will firstly call the function recursively for all the children nodes and then come up with the answer according to the returned values and the value of the current node itself. This process can be regarded as a kind of **postorder** traversal. Typically, a “bottom-up” recursive function **bottom_up(root)**will be something like this:

```python
return specific value for null node
left_ans = bottom_up(root.left)          // call function recursively for left child
right_ans = bottom_up(root.right)        // call function recursively for right child
return answers                           // answer <-- left_ans, right_ans, root.val

```

Let’s go on discussing the question about maximum depth but using a different way of thinking: for a single node of the tree, what will be the maximum depth x of the subtree rooted at itself?
If we know the maximum depth l of the subtree rooted at its **left** child and the maximum depth r of the subtree rooted at its **right** child, can we answer the previous question? Of course yes, we can choose the maximum between them and add 1 to get the maximum depth of the subtree rooted at the current node. That is x = max(l, r) + 1.
It means that for each node, we can get the answer after solving the problem for its children. Therefore, we can solve this problem using a “bottom-up” solution. Here is the pseudocode for the recursive function maximum_depth(root):

```
return 0 if root is null                 // return 0 for null node
left_depth = maximum_depth(root.left)
right_depth = maximum_depth(root.right)
return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root

```

## Example of Bottom Up Recursion - POSTORDER Traversal

```python
class TreeNode:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def countUniValSubTrees(root):
  total_subtrees = helper(root,0)
  return total_subtrees
  
def helper(root,count):
  if node is None:
    return True
   
  left = helper(root.left,count)
  right = helper(root.right,count)
  
  if left and right:
    if (node.left is not None and node.left.val != node.val) or 
        (node.right is not None and node.right.val != node.val):
          return false
    count = count + 1
    return true
    
  return false

```

