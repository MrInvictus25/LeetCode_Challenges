# Given a non-negative integer x, return the square root of x rounded down to the nearest
# integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # It will be the closest digit for sqrt(2)

        leftBoundary = 2
        rightBoundary = x // 2

        while leftBoundary <= rightBoundary:
            guess = leftBoundary + (rightBoundary - leftBoundary) // 2
            number = guess * guess
            if number > x:
                rightBoundary = guess - 1 # Moving to the lower half of the range
            elif number < x:
                leftBoundary = guess + 1 # Moving to the upper half of the range
            else:
                return guess

        return rightBoundary

example = Solution()
print(example.mySqrt(9))
