class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ''
        i = 0
        while num > 0:
            while i < len(roman) and values[i] > num:
                i += 1
            if i < len(roman) and values[i] <= num:
                s = s + roman[i]
                num = num - values[i]
        return s







