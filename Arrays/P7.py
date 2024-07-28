class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        rev = 0
        if x < 0:
            x = (-x)
            while x != 0:
                d = x % 10
                rev = rev * 10 + d
                x = x // 10
            if rev <= pow(2, 31) - 1 and rev >= pow(-2, 31):
                return (-rev)
            return (0)

        else:
            while x != 0:
                d = x % 10
                rev = rev * 10 + d
                x = x // 10
            if rev <= pow(2, 31) - 1 and rev >= pow(-2, 31):
                return (rev)
            return (0)
