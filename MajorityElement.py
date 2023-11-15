# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# APPROACH 1: BRUTE FORCE.
# The brute force algorithm iterates over the array, and then iterates again
# for each number to count its occurrences.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majorityElement = len(nums) // 2
        #print("this is major: ", majorityElement)
        for digit in nums:

            """
            This is a generator expression that generates a sequence of 1s for each number in nums that 
            is equal to the specified digit. It produces a sequence of 1s and 0s, where 1 indicates a 
            match and 0 indicates no match.
            """
            count = sum(1 for number in nums if number == digit)
            if count > majorityElement:
                return digit

example = Solution()
print(example.majorityElement([3,1,3]))

# APPROACH 2: SORT METHOD
# If the elements are sorted in monotonically increasing (or decreasing) order, the majority element
# can be found at index n/2 and n/2 - 1 if n is even
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

example2 = Solution2()
print(example.majorityElement([3,1,3]))

# APPROACH 3: DIVIDE AND CONQUER
# If to imagine the majority element in the left and right halves of an array, I
# can determine which is the global majority element in linear time.
# This approach recurses on the left and right halves of an array until an answer can be trivially achieved
# for a length-1 array. Passing copies of subarrays costs time and space, I instead pass leftPos and
# rightPos indices that describe the relevant slice of the overall array.
class Solution3:
    def majorityElement(self, nums):#, leftPos = 0, rightPos = None):
        def majority_element(leftPos, rightPos):
            if leftPos == rightPos:  # this is case if the only element in an array of size 1
                # is the majority element
                return nums[leftPos]

            middlePos = (rightPos - leftPos) // 2 + leftPos  # Recurse on left and right halves of the slice
            print("This is middlePos: ", middlePos)
            left = majority_element(leftPos, middlePos)
            right = majority_element(middlePos + 1, rightPos)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(leftPos, rightPos + 1) if nums[i] == left)
            right_count = sum(1 for i in range(leftPos, rightPos + 1) if nums[i] == right)
            print("This is left_count: ", left_count)
            print("This is right_count: ", right_count)
            return left if left_count > right_count else right

        return majority_element(0, len(nums) - 1)

example3 = Solution3()
print("This is the third approach")
print(example3.majorityElement([3,1,3]))
