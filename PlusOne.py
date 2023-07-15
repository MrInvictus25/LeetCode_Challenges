# You are given a large integer represented as an integer array digits, where each digits[i]
# is the ith digit of the integer. The digits are ordered from most significant to least significant
# in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Move along the input array starting from the end of array.
#
# Set all the nines at the end of array to zero.
#
# If we meet a not-nine digit, we would increase it by one. The job is done -
# return digits.
#
# We're here because all the digits were equal to nine.
# Now they have all been set to zero.
# We then append the digit 1 in front of the other digits and return the result.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        lengthArray = len(digits)
        for index in range(lengthArray):
            position = lengthArray - 1 - index  # Going through from the end of array
            # print('this is position', position)
            if digits[position] == 9:
                digits[position] = 0
            else:
                digits[position] += 1
                return digits

        digits.insert(0, 1)  # This is case if an array consists of all 9 characters
        return digits

example = Solution()
print(example.plusOne([1,2,9]))

example1 = Solution()
print(example1.plusOne([9]))

example2 = Solution()
print(example2.plusOne([9,9,9]))
