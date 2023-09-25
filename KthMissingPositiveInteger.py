# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        if k <= arr[0]:  #  Checking if the kth missing number is less than the first element of the array.
            return k
        k -= arr[0] - 1 # Decreasing k by the number of positive integers which are missing before the
                        # array starts
        #print(k)
        for element in range(len(arr) - 1):
            #print('element', element)
            missingDigits = arr[element + 1] - arr[element] - 1  # Computation the number of missing positive integers in-between elements
            #print(missingDigits)                             # [element + 1] and element
            if k <= missingDigits: # It means the number to return is in-between arr[element + 1] and arr[element]
                return arr[element] + k
            k -= missingDigits

        return arr[-1] + k  # It is returned because the element to return is greater than the last element of the array

example = Solution()
print(example.findKthPositive([2,3,4,7,11], 5))

example1 = Solution()
print(example.findKthPositive([2,3,4,7,11], 13))
