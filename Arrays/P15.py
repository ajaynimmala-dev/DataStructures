class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums=nums
        nums.sort()
        res=[]
        l=len(nums)
        i=0
        while i!=l-2:
            for j in range(i+1,l):
                for  k in range(i+2,l):
                    if j!=k:
                        if nums[i]+nums[j]+nums[k]==0:
                            s = [nums[i], nums[j], nums[k]]
                            s.sort()
                            if s in res:
                                pass
                            else:
                                res.append(s)
            i+=1
        return res
