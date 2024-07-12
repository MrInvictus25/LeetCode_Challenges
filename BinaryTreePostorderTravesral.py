# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# To return the postorder traversal of a binary tree, you need to visit nodes in the following order:
# left subtree, right subtree, root node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root:TreeNode) -> list[int]:
        if not root:
            return []

        stack = [root]
        result = []  # result is an empty list to store the postorder traversal.

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Stack Behavior: When we pop from the stack, we want to process the right child before the left child so that
            # in the final reversed order, the left child appears before the right child.
            # Order of Processing: By pushing the left child first and the right child second, we ensure that the right
            # child is popped from the stack and processed before the left child.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # Reverse the result list for postorder transversal

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

root.right = node2
node2.left = node3


example = Solution()
print(example.postorderTraversal(root))

