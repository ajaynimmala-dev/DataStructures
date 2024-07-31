class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        while i<len(nums):
            res=nums[i]
            j=i+1
            while j<len(nums) and  nums[j]==res:
                x=nums.pop(j)
            i+=1
        return(len(nums))
    