class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_sum = nums1+nums2
        list_sum.sort()
        return float(median(list_sum))
        