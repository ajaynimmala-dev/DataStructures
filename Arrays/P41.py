class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        nums = set(nums)
        nums = list(nums)
        nums = [x for x in nums if x > 0]
        nums.sort()
        if 1 not in nums:
            return (1)
        else:
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1] + 1:
                    return (nums[i - 1] + 1)
            return (max(nums) + 1)





