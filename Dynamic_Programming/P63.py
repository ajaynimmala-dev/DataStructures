class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res=[]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        value=[]
        def solve(i,j):
            if i==m-1 and j==n-1:
                if obstacleGrid[i][j] != 1:
                    return 1
                else:
                    return 0
            elif i==m or j==n:
                return 0
            elif obstacleGrid[i][j] == 1:
                return 0
            else:
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = str(solve(i+1,j)+solve(i,j+1))
                    return int(obstacleGrid[i][j])
                else:
                    return int(obstacleGrid[i][j])
        return solve(0,0)