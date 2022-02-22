class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        
        for j in range(len(strs[0])):
            count=1
            br=False
            for i in range(1,len(strs)):
                if j< len(strs[i]) and strs[0][j]==strs[i][j]:
                    count+=1
                else:
                    br=True
                    break
            if count==len(strs):
                res+=strs[0][j]
            if br:
                break
        return res
                


                
        