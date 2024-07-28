class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        res = []
        l = len(nums)
        i = 0
        while i != l:
            for j in range(0, l):
                for k in range(0, l):
                    if i != j and j != k and k != i:
                        s = [nums[i], nums[j], nums[k]]
                        s.sort()
                        if nums[i] + nums[j] + nums[k] == 0:
                            if s not in res:
                                res.append(s)
            i += 1
        return res
