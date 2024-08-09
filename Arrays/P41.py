class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        set(nums)
        nums.sort()

        while i<=len(nums):
            if i not in nums:
                return(i)
            i+=1
        return(max(nums)+1)