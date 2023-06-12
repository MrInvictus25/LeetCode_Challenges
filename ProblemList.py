class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate = {}
        for digit in nums:
            if digit in duplicate:
                return True
            else:
                duplicate[digit] = 1
        return False

example = Solution()
print(example.containsDuplicate([1,2,3,4,5,2,2,1]))

class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate = []
        for digit in nums:
            if digit in duplicate:
                return True
            else:
                duplicate.append(digit)
        return False

example = Solution2()
print(example.containsDuplicate([1,2,3,4,5]))
