# Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""  Preorder traversal of a binary tree visits nodes in the following order:
Visit the root node.
Traverse the left subtree in preorder.
Traverse the right subtree in preorder.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        stack = [root] # Initialization a stack with the root node.
        result = [] # The list to store the values of the nodes as we traverse them in preorder.

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                if root.right is not None: # If the current node has a right child, we push it onto the stack
                    stack.append(root.right)
                if root.left is not None:  # If the current node has a left child, we push it onto the stack
                    stack.append(root.left)
            # By pushing the right child before the left child, it allows to ensure that the left child is processed
            # first (since the stack is LIFO - Last In First Out). Because during the pop() is pulled out from the end
        return result

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

example = Solution()
print(example.preorderTraversal(root))
