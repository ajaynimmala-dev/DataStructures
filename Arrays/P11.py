class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height=height
        areas=[]
        for i in range(1,len(height)+1):
            for j in range(i+1,len(height)+1):
                if height[i-1]<height[j-1]:
                    areas.append(height[i-1]*(j-i))
                else:
                    areas.append(height[j-1]*(j-i))
        return(max(areas))