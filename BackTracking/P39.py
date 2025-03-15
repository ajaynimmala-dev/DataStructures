class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = candidates
        nums.sort()
        res = []
        sub = []

        def comb(j, res, sub, target):
            if sum(sub) == target:
                res.append(sub[:])
            else:
                if j >= len(nums) or target < sum(sub):
                    return
                for i in range(j, len(nums)):
                    sub.append(nums[i])
                    comb(i, res, sub, target)
                    sub.pop()
        comb(0, res, sub, target)
        return (res)










