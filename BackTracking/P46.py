class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def solve(sub, res, nums):
            if len(sub) == len(nums):
                res.append(sub[:])
            else:
                for i in range(len(nums)):
                    if nums[i] not in sub:
                        sub.append(nums[i])
                        solve(sub, res, nums)
                        sub.pop()
            return (res)
        return (solve(sub, res, nums))






