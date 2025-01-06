class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            h=len(nums)-1
            while l<h:
                s=nums[i]+nums[l]+nums[h]
                if not(s):
                    sub=[nums[i],nums[l],nums[h]]
                    res.append(sub[:])
                    l+=1
                    h-=1
                    while nums[l]==nums[l-1] and l<h:
                        l+=1
                    while nums[h]==nums[h+1] and l<h:
                        h-=1
                elif s<0:
                    l+=1
                else:
                    h-=1
        return res
