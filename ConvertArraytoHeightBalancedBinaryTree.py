#Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> [TreeNode]:
        def helper(left, right):

            """When we have a sorted array and we are recursively selecting subarrays to construct a binary search tree,
            the condition left > right is used to determine when you have exhausted all elements in a given subarray.
            Returning None indicates that there is no subtree to attach at that position. This is crucial for correctly
            constructing the tree. When the recursion hits the base case and returns None for a subtree, it means that
            the current node will not have a left or right child at that position."""
            if left > right:
                # Base case: If there are no elements to process, return None
                return None

            # Choose the middle element to maintain balance
            middleElement = (left + right) // 2

            # Create the root node for this subtree
            root = TreeNode(nums[middleElement])

            # Recursively build the left subtree
            root.left = helper(left, middleElement - 1)

            # Recursively build the right subtree
            root.right = helper(middleElement + 1, right)

            return root

        # Initial call to helper function with the entire array
        return helper(0, len(nums) - 1)

# This line checks if the script is being run directly (as opposed to being imported as a module in another script).
# If it is being run directly, the code inside this block will execute.
if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    bstRoot = solution.sortedArrayToBST(nums)


    # Function to print the tree in pre-order traversal
    def preOrder(node):
        if not node: # If the current node is None, the function returns immediately (base case for recursion).
            return
        print(node.val, end=' ')
        preOrder(node.left)
        preOrder(node.right)


    preOrder(bstRoot)

""" Example
Consider the array [1, 2, 3]:

    Initial call: helper(0, 2)
        Middle index p = 1, create node with value 2.
        Recursively build left subtree with helper(0, 0):
            Middle index p = 0, create node with value 1.
            Recursively build left subtree with helper(0, -1):
                left > right, return None (no left child).
            Recursively build right subtree with helper(1, 0):
                left > right, return None (no right child).
        Recursively build right subtree with helper(2, 2):
            Middle index p = 2, create node with value 3.
            Recursively build left subtree with helper(2, 1):
                left > right, return None (no left child).
            Recursively build right subtree with helper(3, 2):
                left > right, return None (no right child).
"""
