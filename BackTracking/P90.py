class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(sub, res, k, nums):
            if sub not in res:
                res.append(sub[:])
            for i in range(k, len(nums)):
                sub.append(nums[i])
                res = solve(sub, res, i + 1, nums)
                sub.pop()
            return (res)

        res = []
        sub = []
        res = solve(sub, res, 0, nums)
        return (res)

