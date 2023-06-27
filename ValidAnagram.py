# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            #print(dic)
            #print(dic[i])
        for j in t:
            if j in dic:
                dic[j] -= 1
            #print(dic)
            #print(dic[j])
            else:
                return False
        for check in dic:
            if dic[check] != 0:
                return False

        return True

example = Solution()
print(example.isAnagram("anagram", "nagaram"))
