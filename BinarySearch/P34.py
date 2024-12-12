class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            count_target=nums.count(target)-1
            find_target=nums.index(target)
            return([find_target,find_target+count_target])
        else:
            return([-1,-1])