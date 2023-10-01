# In some array arr, the values were in arithmetic progression:
# the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
# A value from arr was removed that was not the first or last value in the array.
#
# Given arr, return the removed value.

# LINEAR SEARCH
class Solution:
    def missingNumber(self, arr: list[int]) -> int:

        length = len(arr)
        delta = (arr[-1] - arr[0]) // length # Receiving the value of difference using first and the last element
        # print(delta)
        expectedElement = arr[0]

        for digit in arr: # Loop checks if the current value is equal to expected or not
            if digit != expectedElement:
                return expectedElement
            else:
                expectedElement += delta

        return expectedElement

example = Solution()
print(example.missingNumber([5,7,11,13]))

example1 = Solution()
print(example1.missingNumber([15,13,12,11]))


# BINARY SEARCH
class Solution2:
    def missingNumber(self, arr: list[int]) -> int:

        length = len(arr)

        delta1 = (arr[-1] - arr[0]) // length
        leftPointer = 0 # Index of the leftPointer
        rightPointer = length - 1 # Index of the rightPointer
        #print(rightPointer)

        while (leftPointer < rightPointer):
            middlePointer = (rightPointer + leftPointer) // 2

            if arr[middlePointer] == arr[0] + delta1 * middlePointer:  # This formula allows to check correctness of the current element
                                                           # In this case I check the middle element to realize where to perform Binary search
                                                           # on the right of middle pointer or on left side of middle pointer including mid itself.
                leftPointer = middlePointer + 1
            else:
                rightPointer = middlePointer

        return arr[0] + delta1 * leftPointer

example3 = Solution2()
print(example3.missingNumber([2, 4, 6, 8, 10, 14, 16]))
