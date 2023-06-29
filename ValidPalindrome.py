# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        convert = ''.join(re.findall(r'[0-9a-zA-Z]+', s)).lower()
        convertReverse = convert[::-1]
        print(convertReverse)
        return convertReverse == convert

example = Solution()
print(example.isPalindrome("A man, a plan, a canal: Panama"))

example1 = Solution()
print(example.isPalindrome(("race a car")))

example2 = Solution()
print(example.isPalindrome("1b1"))
