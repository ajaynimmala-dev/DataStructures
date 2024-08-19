class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        left=0
        right=len(matrix[0])-1
        top=0
        bottum=len(matrix)-1
        while top<=bottum and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottum+1):
                res.append(matrix[i][right])
            right-=1
            if top<=bottum:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottum][i])
            bottum-=1
            if left<=right:
                for i in range(bottum,top-1,-1):
                    res.append(matrix[i][left])
            left+=1
        return(res)
