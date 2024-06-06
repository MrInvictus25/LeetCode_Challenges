# Definition for a binary tree node.
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

## Example 2
root1 = TreeNode(1)
node2_2 = TreeNode(None)
node3_3 = TreeNode(2)
node4_4 = TreeNode(3)

# Link nodes to form the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

## Example 2

root1.left = node2_2
root1.right = node3_3
node3_3.left = node4_4
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result


example = Solution()
print(example.inorderTraversal(root))

print(example.inorderTraversal(root1))
