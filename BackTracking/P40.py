class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        self.candidates=candidates
        candidates.sort()
        self.target=target
        def solve(sub,res,j,sumi):
            # print(sub,j)
            if sumi==0:
                res.append(sub.copy())
                return
            else:
                if sumi<0:
                    return
                else:
                    for i in range(j,len(candidates)):
                        if i>j and candidates[i]==candidates[i-1]:
                            continue
                        sub.append(candidates[i])
                        solve(sub,res,i+1,sumi-candidates[i])
                        sub.pop()
        solve(sub,res,0,target)
        return res
