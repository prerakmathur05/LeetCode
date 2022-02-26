class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        r=[]
        for num in arr:
            if num==0:
                r.append(0)
                r.append(0)
            else:
                r.append(num)
        for i in range(n):
            arr[i]=r[i]
        

                
        
        