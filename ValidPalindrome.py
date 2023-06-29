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


import re

s = "A man, a plan, a canal: Panama"

pointer = 0  # the left end of the input string from the middle
pointer1 = len(s) - 1   # the right end of the input string from the middle and string index should not be out of range
print(pointer1)

while pointer < pointer1:
    while pointer < pointer1 and not s[pointer].isalnum(): # The isalnum() method returns True if all characters in the string
                                   # are alphanumeric (either alphabets or numbers). If not, it returns False.

        # print(s[2].isalnum())
        pointer += 1
        print(pointer)

    while pointer < pointer1 and not s[pointer1].isalnum():

        pointer1 -= 1
        print(pointer1)

    if s[pointer].lower() != s[pointer1].lower():
        print(False)

    pointer += 1
    pointer1 -= 1

print(True)
