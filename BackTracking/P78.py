class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def call(nums,index,res,sub):
            res.append(sub[:])
            for i in range(index,len(nums)):
                sub.append(nums[i])
                call(nums,i+1,res,sub)
                sub.pop()
            return(res)
        res=[]
        sub=[]
        res=call(nums,0,res,sub)
        return(res)