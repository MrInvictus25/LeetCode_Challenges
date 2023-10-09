# Given two strings needle and haystack, return the index of the first occurrence of needle in
# haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(needle)
        h = len(haystack)

        for first_occurence in range(h - n + 1):  # The starting index of the last substring
            for i in range(h):
                if needle[i] != haystack[first_occurence + i]:
                    break
                if i == n - 1:
                    return first_occurence
        return -1 # This is the case if needle is not part of haystack

example = Solution()
print(example.strStr("sadbutsad","sad"))
example1 = Solution()
print(example1.strStr("leetcode", "leeto"))
