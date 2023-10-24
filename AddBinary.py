# Given two binary strings a and b, return their sum as a binary string.
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        maxLength = max(len(a), len(b))  # Finding a max length among two strings
        a = a.zfill(
            maxLength)  # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length
        b = b.zfill(maxLength)

        carriage = 0
        result = []

        for i in range(maxLength - 1, -1, - 1):  # Iteration through opposite way
            # print(i)
            if a[i] == '1':  # If number a has 1-bit in its lowest bit, we add 1 to the carriage
                carriage += 1
            if b[i] == '1':  # If number a has 1-bit in its lowest bit, we add 1 to the carriage
                carriage += 1

            if carriage % 2 == 1:  # is checking if the rightmost bit of carriage is set to 1. If it's 1,
                # it means that there is a carry to be propagated to the next bit.

                result.append('1')
            else:
                result.append('0')

            carriage //= 2  # This line is used to perform integer division of the carriage variable
            # by 2 and then update the value of the carriage variable with the result.
            # During the loop, bits from the same position in a and b are added to carriage.
            # If carriage becomes 2 or greater, it indicates that a carry is needed to the next bit.
            # If the condition is not met, it means no carry is generated for the current bit addition, so a '0' is appended to the result list.
            # This is a typical approach to adding binary numbers, where the carry is propagated to the next
            # bit when the sum of two bits at the same position exceeds 1

        if carriage == 1:
            result.append('1')
            # print(result)
        result.reverse()

        return "".join(result)

example = Solution()
print(example.addBinary('11', '1'))

example1 = Solution()
print(example1.addBinary('111', '10'))

