class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)!=0:
                    c=i
                    if (c==']' and stack[-1]!='[') or (c=='}' and stack[-1]!='{') or(c==')' and stack[-1]!='('):
                        return(False)
                    else:
                        stack.pop()
                else:
                    return(False)
        if len(stack)==0:
            return(True)
        else:
            return(False)