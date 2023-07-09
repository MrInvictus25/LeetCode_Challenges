# Given two strings s and goal, return true if you can swap two letters in s so the result is equal
# to goal, otherwise, return false

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            collection = {}
            for character in s:
                if character not in collection:  # Collection of characters to keep frequency of each character s
                    collection[character] = 1
                else:
                    collection[character] += 1
                if collection[character] > 1: # If any character has a frequency of more than 1 then we can swap those two same characters
                    return True

        firstIndex = -1 # For storing the indices of string s having different characters than string goal at the same index.
        secondIndex = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIndex == -1: # This is the first index with a different character, we update firstIndex = i
                    firstIndex = i
                    #print(firstIndex)
                elif secondIndex == -1:
                    secondIndex = i
                else:
                    return False
        if secondIndex == -1:  # We can not swap if the character at only one index is different.
            return False

        # All characters of both strings are the same except two indices.
        return s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]

example = Solution()
print(example.buddyStrings("aab", "bab"))
example1 = Solution()
print(example1.buddyStrings("aa", "aa"))


