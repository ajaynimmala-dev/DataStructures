class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi_=nums[0]
        temp=nums[0]
        for i in range(1,len(nums)):
            temp=max(temp+nums[i],nums[i])
            if temp>maxi_:
                maxi_=temp
        return maxi_
