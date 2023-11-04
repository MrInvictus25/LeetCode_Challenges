# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it

# Memory-efficient Dynamic Programming
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        row = [1]

        for i in range(rowIndex):
            # print("this is i:", i)
            for j in range(i, 0, -1): # It is necessary to keep all read accesses on the previous row value of pascal[j],
                # before any write access to pascal[j] for the current row value.
                # That's possible by evaluating each row from the end, instead of the beginning.
                # Thus, a new row value of pascal[j+1] must be generated before doing so for pascal[j].
                # print("this is j:", j)
                row[j] = row[j] + row[j-1]
                # print("this is row:", row)
            row.append(1)
            # print("this is row after append:", row)
        return row

example = Solution()
print(example.getRow(3))


