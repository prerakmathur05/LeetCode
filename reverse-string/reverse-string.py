class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reversing(start,end,s):
            if start>=end:
                return 
            s[start],s[end]=s[end],s[start]
            return reversing(start+1,end-1,s)
        reversing(0, len(s)-1,s)
            