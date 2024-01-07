# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase
# and uppercase characters.
# Print True if  has any alphanumeric characters. Otherwise, print False.
# Print True if  has any alphabetical characters. Otherwise, print False.
# Print True if  has any digits. Otherwise, print False.
# Print True if  has any lowercase characters. Otherwise, print False.
# Print True if  has any uppercase characters. Otherwise, print False

class Solution():
    def validador(self, s: str) -> bool:
        #s = input()

        print(any(char.isalnum() for char in s))

        print(any(char.isalpha() for char in s))

        print(any(char.isdigit() for char in s))

        print(any(char.islower() for char in s))

        print(any(char.isupper() for char in s))

example = Solution()
example.validador("ql1")
