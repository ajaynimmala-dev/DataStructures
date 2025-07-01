class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        temp=dict()
        i=0
        nums.sort()
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        def solve(sub,res):
            if len(sub)==len(nums):
                res.append(sub.copy())
            else:
                for i in temp:
                    if temp[i]==0:
                        continue
                    else:
                        sub.append(i)
                        temp[i]-=1
                        solve(sub,res)
                        temp[i]+=1
                        sub.pop()
        solve(sub,res)
        return res
