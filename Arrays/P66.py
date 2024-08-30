class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 1
        res = 0
        final = []
        while i <= len(digits):
            res = res + digits[i - 1] * pow(10, len(digits) - i)
            i += 1
        res += 1
        while res != 0:
            d = res % 10
            final.append(d)
            res = res // 10
            print(final)
        final.reverse()
        return (final)

