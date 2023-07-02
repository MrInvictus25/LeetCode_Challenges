# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
# two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote
# the elements that should be merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        nums1Copy = nums1[:m]  # Coping the first m values of nums1
        # [1, 2, 3]
        ReadPointer1 = 0  # Initialization read pointer to the beginning of nums1Copy
        ReadPointer2 = 0  # Initialization read pointer to the beginning of nums2
        WritePointer = 0  # Initialization read pointer to the beginning of nums1

        for WritePointer in range(n + m):  # The length of nums1 list
            #print(WritePointer)
            #print('=' * 50)
            if ReadPointer2 >= n or (ReadPointer1 < m and nums1Copy[ReadPointer1] <= nums2[ReadPointer2]):  # Reading values from nums1Copy
                nums1[WritePointer] = nums1Copy[ReadPointer1]  # The case when we keep element from the nums1 list
                # print('This is WritePointer: ', nums1[WritePointer])
                # print('=' * 50)
                # print('This is ReadPointer: ', nums1Copy[ReadPointer1])
                # print('=' * 50)

                ReadPointer1 += 1
            else:
                nums1[WritePointer] = nums2[ReadPointer2]  # The case when we add element from the nums2 list
                ReadPointer2 += 1

        WritePointer += 1

        return nums1

example = Solution()
print(example.merge([1,2,3,0,0,0], 3, [2,5,6],3))




