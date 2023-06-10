class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]  # Taking the first item as a prefix
        #print(prefix[:-1])
        #print(strs[2].find('fl'))
        for item in range(1, len(strs)):  # Iterating all items excluding the firs one (assigned prefix)

            while strs[item].find(prefix) != 0: # Checking on presence the first occurrence of the current prefix
                prefix = prefix[:-1]  # Eliminating the last letter


                if prefix == "":  # If all letters were eliminated, consequently there are a common prefix
                    return "There is not a common prefix"

        return prefix

example = Solution()
print(example.longestCommonPrefix(["flower","flow","flight"]))

