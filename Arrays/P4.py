class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1=nums1
        self.nums2=nums2
        nums1=nums1+nums2
        nums1.sort()
        if len(nums1)%2==0:
            return((nums1[len(nums1)//2]/2.0)+(nums1[len(nums1)//2-1])/2.0)
        else:
            return(nums1[(len(nums1)//2)])