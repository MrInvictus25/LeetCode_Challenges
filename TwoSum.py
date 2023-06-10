# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i, j in enumerate(nums):
            #print("This is an element inside a list:", j)
            #print("This is a indice of the element inside a list:", i)
            result = target - j
            #print(result)
            if result in dic:
                return [dic[result], i]  # Returning the indices of the two numbers in list
            dic[j] = i  # Adding an element in dictionary
            print(dic)

example = Solution()
print(example.twoSum([2,4,7,1],8))

example1 = Solution()
print(example1.twoSum([0,2,6,5],8))


# a = [2,4,7,1]
# for i in range(len(a)):
#     print(i)
#     for j in range(len(a)):
#         print(j)
print(50 * '=')
dicti = {}
dicti[2] = 0
dicti[3] = 2
dicti[5] = 4
b = dicti[5]
print(b)
print(dicti)
