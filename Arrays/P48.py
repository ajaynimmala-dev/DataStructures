class Solution(object):
def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = []
    l = len(matrix)
    for i in range(l):
        j = l - 1
        r = []
        while j >= 0:
            r.append(matrix[j][i])
            j -= 1
        matrix.append(r)
    del matrix[0:l]
    return (matrix)

