class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=nums1+nums2
        s.sort()
        t=len(s)
        if t%2==0:
            return (s[t//2-1]+s[t//2])/2.0
        else:
            return s[t//2]
