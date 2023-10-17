# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# It is necessary to write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        leftPointer = 0  # (0)
        rightPointer = len(nums) - 1  # (3)

        while leftPointer <= rightPointer:
            middleIndex = (leftPointer + rightPointer) // 2  # (1)
            print(middleIndex)
            if nums[middleIndex] == target:
                return middleIndex
            if target < nums[middleIndex]:
                rightPointer = middleIndex - 1
            else:
                leftPointer = middleIndex + 1
        return leftPointer

example = Solution()
print(example.searchInsert([1,3,5,6], 6))
