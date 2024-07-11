# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
# There are three primary types of DFS traversals in a binary tree: pre-order, in-order, and post-order. For the problem
# of checking if there is a root-to-leaf path with a sum equal to a target value, we typically use a pre-order traversal
# because it allows us to process the current node and its children in a natural order.
"""  Preorder traversal of a binary tree visits nodes in the following order:
Visit the root node.
Traverse the left subtree in preorder.
Traverse the right subtree in preorder.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]
        while stack:
            node, currSum = stack.pop()
            if not node.left and not node.right and currSum == 0:
                return True
            #  if I append the right child first and then the left child, the left child will be processed before the
            #  right child because the stack is a Last-In-First-Out (LIFO) data structure.

            if node.right: # Checks if the current node has a right child.
                stack.append((node.right, currSum - node.right.val)) # If it does, appends the right child and the updated curr_sum (subtracting the right child’s value) to the stack.
            if node.left: # Checks if the current node has a left child.
                stack.append((node.left, currSum - node.left.val)) # If it does, appends the left child and the updated curr_sum (subtracting the right child’s value) to the stack.
        return False

root = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)


root.left = node2
root.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.right = node9

example = Solution()
print(example.hasPathSum(root, 22))
