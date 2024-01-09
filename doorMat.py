# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
class Solution():
    def doorMat(self, N: int, M: int):

        # print('This is N', N)
        # print('This is N', M)

        # Drawing the top part
        for i in range(N // 2):
            # print('this is i', i)
            j = int((2 * i) + 1)
            # print('this is j', j)
            print(('.|.' * j).center(M, '-'))

        print('WELCOME'.center(M, '-'))  # Printing 'WELCOME' sign

        # Drawing the bottom part
        for i in reversed(range(N // 2)):
            j = int((2 * i) + 1)
            print(('.|.' * j).center(M, '-'))

        return ' '
example = Solution()
print(example.doorMat(7, 21))
