# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Traversal: Visiting all the nodes in a specific order.
# In an inorder traversal, the nodes are visited in the following order:
# Traverse the left subtree.
# Visit the root node.
# Traverse the right subtree.


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

#print(root.val)

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        result = []
        stack = []  #  Stack is an empty list used to keep track of nodes
        current = root # Setting current to the root node.
        #print(current.val)

        while current or stack:
            while current:
                #print(current.val)
                stack.append(current) # This line is used to keep track of the nodes I need to process later
                current = current.left # Moving from current to current.left (node 2 and so on).
                #print("left side: ", current.val)

            current = stack.pop()
            #print(current.val)
            result.append(current.val)
            current = current.right # Updating the current pointer to the right child of the popped node
            #print(result)
        return result


example = Solution()
print(example.inorderTraversal(root))

print(example.inorderTraversal(root1))
