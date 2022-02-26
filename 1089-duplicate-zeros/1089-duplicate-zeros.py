class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        i=0
        while i<n:
            if arr[i]==0:
                j=n-2
                while j>i:
                    arr[j+1]=arr[j]
                    j-=1
                if i<n-1:
                    arr[i+1]=0
                i+=1
            i+=1
        return arr
            
        