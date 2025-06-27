class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[[0]*n for _ in range(m)]
        def unique(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif i==m or j==n:
                return 0
            else:
                if res[i][j] == 0:
                    res[i][j]=unique(i+1,j)+unique(i,j+1)
                    return res[i][j]
                else:
                    return res[i][j]
        return unique(0,0)
        # return r