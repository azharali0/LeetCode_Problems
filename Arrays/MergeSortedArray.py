class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :type: None Do not return anything, modify nums1 in-place instead.
        """
        i = m
        for x in nums2:
            nums1[i] = x
            i+=1
        nums1.sort()
        return nums1