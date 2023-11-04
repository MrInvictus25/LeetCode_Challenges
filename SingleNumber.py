# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# THE FIRST SOLUTION (THAT SATISFIES THE CONDITION ABOVE):

# (eXclusive OR) A Boolean logic operation that is widely used in cryptography as well as in generating
# parity bits for error checking and fault tolerance. XOR compares two input bits and generates one
# output bit. The logic is simple. If the bits are the same, the result is 0.
# If the bits are different, the result is 1.

class Solution(object):
    def singleNumber(self, nums):

        digit = 0
        for i in nums:
            digit ^= i
        return digit

example = Solution()
print(example.singleNumber([2,2,1]))

# THE SECOND SOLUTION
class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        singleDigit = []

        for digit in nums:
            if not digit in singleDigit:
                singleDigit.append(digit)
            else:
                singleDigit.remove(digit)

        return singleDigit.pop()

example2 = Solution2()
print(example2.singleNumber([4,1,2,1,2]))

# THE THIRD SOLUTION

from collections import defaultdict  # It provides a default value for keys that have not been assigned a value yet.
class Solution3:
    def singleNumber(self, nums: list[int]) -> int:
        dictDigit = defaultdict(int)  # defaultdict(int) initializes a defaultdict with a default
        # value of int(), which is 0.
        for i in nums:
            dictDigit[i] += 1
            print(dictDigit)
        for i in dictDigit:
            if dictDigit[i] == 1:
                return i
example3 = Solution3()
print(example3.singleNumber([4,1,2,1,2]))

