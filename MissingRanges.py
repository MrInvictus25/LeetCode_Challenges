# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
#
# Return the shortest sorted list of ranges that exactly covers all the missing numbers.
# That is, no element of nums is included in any of the ranges, and each missing number is covered
# by one of the ranges.
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        n = len(nums)  # Creating a variable n and initialize it to the size of nums
        absentRanges = []  # It will contain the output

        if len(nums) == 0:
            absentRanges.append([lower, upper])
            return absentRanges

        if lower < nums[0]:  # Checking if the first element of the array is equal to lower or not
            absentRanges.append([lower, nums[0] - 1])  # There is a missing range, it is added to 'absentRanges'

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:  # It means there are no missing numbers between these two numbers
                continue
            else:
                # nums[i + 1] - nums[i] > 1 # It means there are missing numbers between these two numbers
                absentRanges.append([nums[i] + 1, nums[i + 1] - 1])

        if nums[n - 1] < upper:  # Checking if the last element of the array is equal to upper or not
            absentRanges.append([nums[n - 1] + 1, upper])  # It means there is a missing range

        return absentRanges

example = Solution()
print(example.findMissingRanges([0,1,3,50,75], 0, 99))

example1 = Solution()
print(example1.findMissingRanges([0,2,10,41,85], 0, 99))
