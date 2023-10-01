# In some array arr, the values were in arithmetic progression:
# the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
# A value from arr was removed that was not the first or last value in the array.
#
# Given arr, return the removed value.


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
