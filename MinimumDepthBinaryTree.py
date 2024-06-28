# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        """Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends 
        of the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list 
        that provides O(n) time complexity.
        """
        container = collections.deque([root]) # A queue container (using collections.deque) is initialized with the root node.
        depth = 1
        while container:
            numberNodes = len(container) # numberNodes is set to the number of nodes at the current depth level.
            for number in range(numberNodes): # Iterating over all nodes at the current depth level.
                node = container.popleft()
                if not node: # If the node is None, skip it.
                    continue
                # The first leaf would be at minimum depth, hence return it.
                if not node.left and not node.right:
                    # Since this is the first leaf node encountered at the current depth, return the current depth as the minimum depth.
                    return depth
                # Adding the left and right children of the current node to the queue for processing at the next depth level.
                container.append(node.left)
                container.append(node.right)
            depth += 1 # Incrementing the depth after processing all nodes at the current depth level.

    # if the while loop ends without finding a leaf (which theoretically shouldn't happen in a valid binary tree), return -1.
        return -1

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
print(example.minDepth(root))



