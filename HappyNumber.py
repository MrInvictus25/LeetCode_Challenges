# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Approach: Detecting Cycles with a HashSet
"""
Three possible following links to the end:
- It eventually gets to 111.
- It eventually gets stuck in a cycle.
- It keeps going higher and higher, up towards infinity (It is necessary to think carefully about what the largest next
number we could get for each number of digits is). For Instance:
Digit - 1, Largest - 9, Next - 81 | Digit - 2, Largest - 99, Next - 162 | Digit - 3, Largest - 999, Next - 243 |
Digit - 4, Largest - 9999, Next - 324 | Digit - 13, Largest - 9999999999999, Next - 1053

For a number with 3 digits, it's impossible to exceed 243. It means it will ought to either get stuck in a cycle below 243
or go down to 1. Numbers with 4 or more digits will always lose a digit at each step until they are down to 3 digits.
"""
class Solution():
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                """
                it separates the last digit of the number stored in the variable n and assigns it to the variable digit, 
                while updating n to be the remaining part of the original number
                """
                n,digit = divmod(n, 10)  # The divmod() function returns a tuple containing the quotient  and the remainder when argument1
                total += digit ** 2     # (dividend) is divided by argument2 (divisor).
                print("This is the total", total)
            return total

        existDigits = set()
        while n != 1 and n not in existDigits:
            existDigits.add(n)
            print("This is existDigits", existDigits)
            n = getNext(n)
            print("This is n", n)
        return n == 1

example = Solution()
print(example.isHappy(19))



