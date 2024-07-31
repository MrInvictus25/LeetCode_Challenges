# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# Return k.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # Two indexes approach. The first index updates the value in our input array while reading
        # the data from the second index

        writingIndex = 1  # The first presence of an integer
        readingIndex = len(nums)
        test = []
        for i in range(1, readingIndex):  # To start with 0 element during finding the unique element.
            if nums[i - 1] != nums[i]:  # Finding different. Otherwise, it will take the last element in an array
                nums[writingIndex] = nums[i]
                writingIndex += 1
                #test.append(nums[i])
                #print(test)
        return writingIndex  # the number of unique elements in nums

example = Solution()
print(example.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

example1 = Solution()
print(example1.removeDuplicates([1,1,1,1,1]))

example2 = Solution()
print(example1.removeDuplicates([1,2,3,6,7]))
