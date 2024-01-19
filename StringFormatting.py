
class Solution():
    def print_formatted(self, number: int) -> int:

        width = len("{0:b}".format(number)) # format method to create a binary representation of the number variable.
        # {0:b}: This is a placeholder in a string for formatting. The 0 inside the curly braces refers to the index of
        # the argument passed to the format method. The :b inside the curly braces specifies the formatting option.
        for digit in range(1, number + 1):

        #print('dex: {:d}'.format(digit))
        #print('oct: {:o}'.format(digit))
        #print('Hex: {:X}'.format(digit))
        #print('bin: {:b}'.format(digit))
            print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(digit, width=width))
             # {0} refers to the first argument passed to the format method (in this case, digit), and {width} is a nested
        # # placeholder representing the width of the field, which is specified later in the format method.
example = Solution()
example.print_formatted(5)


width = len("{1:b}".format(4, 5))
print(width)
