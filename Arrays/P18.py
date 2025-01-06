class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                h = len(nums) - 1
                while l < h:
                    s = nums[i] + nums[j] + nums[l] + nums[h]
                    if s == target:
                        sub = [nums[i], nums[j], nums[l], nums[h]]
                        sub.sort()
                        if sub not in res:
                            res.append(sub[:])
                        else:
                            l += 1
                            h -= 1
                    elif s > target:
                        h -= 1
                    else:
                        l += 1
        return res


