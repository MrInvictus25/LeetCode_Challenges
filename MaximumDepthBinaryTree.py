# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create individual nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)


# Link nodes to form the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5


class Solution:
    def maxDepth(self, input) -> int:
        if input is None:
            print("No children")
            return 0
        else:

            # Recursion calculates the maximum depth of the left and right subtrees
            left_depth = self.maxDepth(input.left)
            print("This is left side: ", left_depth)
            right_depth = self.maxDepth(input.right)
            print("This is right side: ", right_depth)
            print("Answer:", max(left_depth, right_depth) + 1)
            return max(left_depth, right_depth) + 1

example = Solution()
print(example.maxDepth(root))
