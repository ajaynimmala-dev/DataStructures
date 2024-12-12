class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
                """
        if target in nums:
            if nums[0]<=target and target<=max(nums):
                return(nums.index(target))
            elif target>=(min(nums)) and target<=nums[-1]:
                return(nums.index(target))
        return(-1)
