class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        i = 0
        res = []
        while i != (len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            x = [nums[i], nums[j], nums[k], nums[l]]
                            x.sort()
                            if x not in res:
                                res.append(x)

            i += 1
        return (res)
