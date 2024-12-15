class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        final_res=[]
        i=0
        while i<len(strs):
            x=sorted(strs[i])
            temp_res=[]
            j=i+1
            while j<len(strs):
                if(len(strs[i])==len(strs[j])):
                    y=sorted(strs[j])
                    if x==y:
                        temp_res.append(strs[j])
                        strs.pop(j)
                    else:
                        j+=1
                else:
                    j+=1
            temp_res.append(strs[i])
            strs.pop(i)
            final_res.append(temp_res)
        return(final_res)



