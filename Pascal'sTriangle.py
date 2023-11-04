# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above.

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascalTriangle = []

        for rowNumber in range(numRows):
            print("this is rownumber: ", rowNumber)

            row = [None for none in range(rowNumber + 1)] # Constructing a shape
            row[0], row[-1] = 1, 1  # The first and last row elements are always 1.
            print("this is row: ", row)
            print("this is len", len(row))
            for i in range(1, len(row) - 1):
                print("this is i", i)
                print("this is pascalTriangle[rowNumber - 1][i - 1]: ", pascalTriangle[rowNumber - 1][i - 1])
                print("This is pascalTriangle[rowNumber - 1][i]: ", pascalTriangle[rowNumber - 1][i])
                row[i] = pascalTriangle[rowNumber - 1][i - 1] + pascalTriangle[rowNumber - 1][i] #  The finding of the each number by summing of the two numbers directly above it

            print("this is row: ", row)
            print(pascalTriangle)
            pascalTriangle.append(row)
            print("this is pascal after append: ", pascalTriangle)

        return pascalTriangle

example = Solution()
print(example.generate(5))
