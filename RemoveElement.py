
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums
# which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need
# to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not
# equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        writingIndex = 0
        readingIndex = len(nums)

        while writingIndex < readingIndex:
            if nums[writingIndex] == val:  # Finding different.
                nums[writingIndex] = nums[readingIndex-1] # Overriding the element in the array
                readingIndex -= 1
                #print(nums)
                #nums.pop(i)
            else:
                writingIndex += 1
                #print(nums)


        return readingIndex  # the number of elements in nums which are not equal to val.


example = Solution()
print(example.removeElement([3,2,2,3], 3))

example2 = Solution()
print(example2.removeElement([0,1,2,2,3,0,4,2], 2))

# The Second solution
class Solution1:
    def removeElement(self, nums: list[int], val: int) -> int:

        writingIndex = 0
        readingIndex = len(nums)

        for i in range(1, readingIndex + 1):
            if nums[i - 1] == val:
                writingIndex += 1
        return len(nums) - writingIndex

example3 = Solution1()
print(example3.removeElement([3,2,2,3], 3))

example4 = Solution()
print(example4.removeElement([0,1,2,2,3,0,4,2], 2))
