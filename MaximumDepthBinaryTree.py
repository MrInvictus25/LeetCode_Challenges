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
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            print("No children")
            #print("This is current in if: ", root.val)
            print("="*50)
            return 0
        else:
            # Recursion calculates the maximum depth of the left and right subtrees
            left_depth = self.maxDepth(root.left)
            print("This is current in else left: ", root.val)
            print("This is left side: ", left_depth)
            print("=" * 50)
            right_depth = self.maxDepth(root.right)
            print("This is current in else right: ", root.val)
            print("This is right side: ", right_depth)
            print("=" * 50)
            return max(left_depth, right_depth) + 1

print("start")
example = Solution()
print(example.maxDepth(root))
print("finish")



### The second solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [(root, 1)]  # Stack holds tuples of (node, current_depth)
        max_depth = 0 # To keep track of the maximum depth encountered during traversal.

        while stack:
            print("This is len", len(stack))
            node, depth = stack.pop()
            print("This is node", node)
            print("This is depth", depth)
            if node:
                max_depth = max(max_depth, depth)
                print("This is max_depth", max_depth)
                print("=" * 50)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth

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
print(example.maxDepth(root))

