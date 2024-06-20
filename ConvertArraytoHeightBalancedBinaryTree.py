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

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    bstRoot = solution.sortedArrayToBST(nums)


    # Function to print the tree in pre-order traversal
    def preOrder(node):
        if not node:
            return
        print(node.val, end=' ')
        preOrder(node.left)
        preOrder(node.right)


    preOrder(bstRoot)

