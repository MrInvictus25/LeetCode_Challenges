class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### AN Iterative approach -  An iterative approach  involves using a queue (or a stack) to perform a level-order
# traversal while comparing nodes in pairs.
# Symmetric tree might be considered if we confirm that left.val == right.val and the left child of the left (left.left.val) is
# the same as the right child of the right (right.right.val)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        queue = [root, root] # By adding the root node twice to the queue, we are essentially setting up the first pair
        # of nodes to compare. This allows us to treat the root's left and right children as the first two nodes to be checked for symmetry.

        while queue:
            subnode1 = queue.pop(0)  # Removing the first two nodes from the queue for comparison to move to next node
            subnode2 = queue.pop(0)

            if subnode1 is None and subnode2 is None:
                continue  # If both nodes are None, they are symmetric, we can continue to the next pair
            if subnode1 is None or subnode2 is None:
                return False  # If only one of the nodes is None, they are not symmetric
            if subnode1.val != subnode2.val:
                return False # If the values of the nodes are different, they are not symmetric
            queue.append(subnode1.left)  # Enqueue the left child of the first node
            queue.append(subnode2.right)  # Enqueue the right child of the second node
            queue.append(subnode1.right)  # Enqueue the right child of the first node
            queue.append(subnode2.left)  # Enqueue the left child of the second node
            # queue.extend([subnode1.left, subnode2.right])
            # queue.extend([subnode1.right, subnode2.left])
        return True


# Create individual nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

# Link nodes to form the tree
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


example = Solution()
print(example.isSymmetric(root))
