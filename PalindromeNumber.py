# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            print(revertedNumber)
            x //= 10
            print(x)
        return x == revertedNumber or x == revertedNumber//10

example = Solution()
print(example.isPalindrome(1551))




