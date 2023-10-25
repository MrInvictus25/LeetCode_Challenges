# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascalTriangle = []

        for rowNumber in range(numRows):
            row = [None for none in range(rowNumber + 1)]
            row[0], row[-1] = 1, 1  # The first and last row elements are always 1.
            # print(range(rowNumber + 1))
            # print(row)
            for i in range(1, len(row) - 1):
                row[i] = pascalTriangle[rowNumber - 1][i - 1] + pascalTriangle[rowNumber - 1][i]

            pascalTriangle.append(row)

        return pascalTriangle

example = Solution()
print(example.generate(5))
