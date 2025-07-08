class Solution:
    def numTrees(self, n: int) -> int:
        def fact(n):
            if n == 1:
                return 1
            else:
                return n * fact(n - 1)

        temp1 = fact(2 * n)
        temp2 = fact(n)
        return int((temp1 / pow(temp2, 2)) / (n + 1))

