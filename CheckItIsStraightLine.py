class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        xDelta = coordinates[1][0] - coordinates[0][0] # Difference between x2 and x1
        yDelta = coordinates[1][1] - coordinates[0][1]  # Difference between y2 and y1

        for item in range(1, len(coordinates)): # Check if the slope between points 0 and i, is the same as between 0 and 1.

            xNext = coordinates[item][0] # Assigning a new variable to compare the slope
            yNext = coordinates[item][1]

            if yDelta * (xNext - coordinates[1][0]) != (yNext - coordinates[1][1]) * xDelta:
                return False

            #print(coordinates[item])

        return True

example = Solution()
print(example.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
