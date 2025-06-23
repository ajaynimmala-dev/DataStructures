class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for p in range(numRows)]
        n = numRows - 1
        i = 0
        if len(s) == 1 or numRows == 1:
            return s
        while i < len(s):
            if n != numRows - 1 and n != 0:
                res[n].append(s[i])
                i += 1
                n -= 1
            else:
                n = numRows - 1
                for k in range(len(res)):
                    if i < len(s):
                        res[k].append(s[i])
                        i += 1
                    else:
                        break
                n -= 1
        j = 0
        print(res)
        temp1 = []
        for i in res:
            if len(i) == 0:
                break
            temp1.append(reduce(lambda x, y: x + y, i))
        temp = reduce(lambda x, y: x + y, temp1)
        return temp









