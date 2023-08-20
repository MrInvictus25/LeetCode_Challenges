# Given an array nums containing n distinct numbers in the range [0, n], return the only
# number in the range that is missing from the array.

# The first solution
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        # print(array)

        if nums[-1] != len(nums):  # Checking that n is at the last index
            # print("len does not equal a len of an array")
            return len(nums)

        elif nums[0] != 0:  # Checking that 0 is at the first index
            return (0)

        for i in range(1, len(nums)):  # Comparing sequentually each element with its index
            # missingDigit = nums[i - 1] + 1
            if nums[i] != i:
                return i
example = Solution()
print(example.missingNumber([3,0,1]))
example1 = Solution()
print(example1.missingNumber([7,2,5,0,1,3,6]))

print('=' * 25)

# The second solution. Gauss's Formula
class Solution1:
    def missingNumber(self, nums: list[int]) -> int:
        totalSum = len(nums) * (len(nums) + 1) // 2
        currentSum = sum(nums)

        return totalSum - currentSum

example2 = Solution()
print(example2.missingNumber([3,0,1]))
example3 = Solution()
print(example3.missingNumber([7,2,5,0,1,3,6]))
