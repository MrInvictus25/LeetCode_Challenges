# You are given an array of characters letters that is sorted in non-decreasing order,
# and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

# In binary search, we repeatedly divide the solution space where the answer could be in half until
# the range contains just one element.

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        rangeLeft = 0  # Initialization it to the starting index 0
        rangeRight = len(letters) - 1  # Initialization it to the last index

        while rangeLeft <= rangeRight:
            rangeMiddle = (rangeLeft + rangeRight) // 2
            if letters[rangeMiddle] <= target:
                rangeLeft = rangeMiddle + 1  # Moving to the upper half of the range
            else:
                rangeRight = rangeMiddle - 1  # Moving to the lower half of the range as all the characters
                            # at indices greater or equal to rangeMiddle would also be greater than target

        #if rangeLeft == len(letters):  # it means there is no character in letters that is lexicographically greater
                                # than target. rangeLeft attains the end of the range
            # return letters[0]

        if rangeLeft > rangeRight: # rangeLeft denotes the index of the smallest character that is lexicographically greater
             # than target. This is because all characters at indices greater than right would be greater than target
            return letters[rangeLeft]
        else:
            return letters[0]

example = Solution()
print(example.nextGreatestLetter(["c","f","j"], "c"))

example1 = Solution()
print(example1.nextGreatestLetter(["c","f","j"], "a"))
