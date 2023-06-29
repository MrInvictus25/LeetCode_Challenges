class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:


        writingIndex = 1  # The first presence of an integer
        readingIndex = len(nums)

        for i in range(1, readingIndex):  # To start with 0 element during founding the unique element.
            if nums[i - 1] != nums[i]:  # Otherwise, it will take the last element in an array
                nums[writingIndex] = nums[i]
                writingIndex += 1
        return writingIndex  # the number of unique elements in nums

example = Solution()
print(example.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

