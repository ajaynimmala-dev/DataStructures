class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            res.append(nums[i])
            for j in range(i + 1, len(nums)):
                x = sum([nums[k] for k in range(i, j + 1)])
                res.append(x)
        return (max(res))