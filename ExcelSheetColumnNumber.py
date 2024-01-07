# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        # dict = { key:value for key, value in <sequence> if <condition> }
        collection = {chr(i + 65): i + 1 for i in range(26)} # Dictionary comprehension to design a collection of alphabet.
        print(collection)                        #  Decimal 65 in ASCII table corresponds to char 'A'

        value = str(columnTitle)
        #print("This is a value: ", value)
        #print("This is a len of value: ", len(value))
        for number in range(len(value)):
            #print("This is a char: ", char)

            existChar = value[len(value) - 1 - number]
            #print("This is a existChar: ", existChar)

            result += (collection[existChar] * (26 ** number))

        return result
example = Solution()
print(example.titleToNumber('AA'))


