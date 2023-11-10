# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1 # It effectively maps the numeric value of the column to its corresponding letter representation.
            # By decrementing columnNumber before the conversion to a letter, it aligns the numeric
            # representation to the alphabetical sequence.
            letter = chr(ord('A') + columnNumber % 26) # ord('A') retrieves the ASCII value of 'A', which is 65.
            # columnNumber % 26 computes the remainder of columnNumber when divided by 26, ensuring that the value
            # remains within the range of 0 to 25 (representing the alphabet). It takes 'A' as a starting point, then shifts
            # the letter by an amount equal to columnNumber % 26 while ensuring the output falls within  the range of 0 to 25
            #print("This is ord('A')", ord('A'))
            print("This is a letter", letter)
            result.append(letter)
            columnNumber //= 26 # By dividing it by 26 and updating the value of columnNumber for the next iteration of the loop.
            print(columnNumber)
        return ''.join(reversed(result))

example = Solution()
print(example.convertToTitle(27))
example1 = Solution()
print(example1.convertToTitle(2023))
