# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution():
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                n,digit = divmod(n, 10)  # The divmod() function returns a tuple containing the quotient  and the remainder when argument1
                total += digit ** 2     # (dividend) is divided by argument2 (divisor).

            return total

        existDigits = set()
        while n != 1 and n not in existDigits:
            existDigits.add(n)
            n = getNext(n)

        return n == 1

example = Solution()
print(example.isHappy(19))

