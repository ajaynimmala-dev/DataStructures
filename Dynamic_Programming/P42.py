class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = []
        max_right = []
        max_left.append(0)
        max_right.append(0)
        for i in height[0:len(height) - 1]:
            max_left.append(max(max_left[-1], i))
        for i in height[-1:-len(height) - 1:-1]:
            max_right.insert(0, max(max_right[0], i))
        k = 0
        trap = []
        for i, j in zip(max_left, max_right):
            temp = min(i, j)
            if temp - height[k] <= 0:
                k += 1
                continue
            else:
                trap.append(temp - height[k])
                k += 1
        return sum(trap)

