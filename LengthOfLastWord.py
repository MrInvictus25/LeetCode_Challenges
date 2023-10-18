# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal  substring consisting of non-space characters only.


# SOLUTION number 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trailSpace = len(s) - 1
        length = 0

        while trailSpace >= 0 and s[trailSpace] == ' ':  # This loop is used to locate the last word
            trailSpace -= 1
            #print("ts after 1 loop", trailSpace)

        while trailSpace >= 0 and s[trailSpace] != ' ':  # This loop is used to calculate its length.
            trailSpace -= 1
            #print("ts after 2 loop", trailSpace)
            length += 1

        return length


# SOLUTION number 2
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        trailSpace = len(s) - 1
        length = 0

        while trailSpace > 0:
            trailSpace -= 1

            if s[trailSpace] != ' ':
                length += 1
            elif length > 0:
                return length

        return length

# SOLUTION number 3
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
