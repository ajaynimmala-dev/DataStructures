class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(len(nums)):
            res = max(nums[i], res)
            for j in range(i + 1, len(nums)):
                x = sum([nums[k] for k in range(i, j + 1)])
                res = max(res, x)
        return (res)
