# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        maxLength = max(len(a), len(b))  # Finding a max length among two strings
        a = a.zfill(
            maxLength)  # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length
        b = b.zfill(maxLength)

        carriage = 0  # This is a variable that keeps track of whether there is a carry when adding the corresponding bits of a and b.
        result = []

        for i in range(maxLength - 1, - 1, - 1):  # Iteration through opposite way
            if a[i] == '1':  # If number a has 1-bit in its lowest bit, we add 1 to the carriage
                carriage += 1
            if b[i] == '1':  # If number a has 1-bit in its lowest bit, we add 1 to the carriage
                carriage += 1

            if carriage % 2 == 1:  # Appending the lowest bit of the carriage to the answer, and moving the highest bit of the carriage to the next order bit.
                result.append('1')
            else:
                result.append('0')
                # print('car: ', carriage)
                # print('result: ', result)

            carriage //= 2

        if carriage == 1:
            result.append('1')
            # print(result)
        result.reverse()

        return "".join(result)

example = Solution()
print(example.addBinary('11', '1'))

example1 = Solution()
print(example1.addBinary('111', '10'))


print(2//2)
