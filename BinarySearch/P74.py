class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target >= i[0] and target <= i[len(i) - 1]:
                low, high = (0, len(i) - 1)
                while low <= high:
                    mid = (low + high) // 2
                    if i[mid] == target:
                        return True
                    elif target > i[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False
