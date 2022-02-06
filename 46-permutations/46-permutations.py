class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(first):
            if first==n:
                res.append(nums[:])
            for j in range(first,n):
                nums[first],nums[j]=nums[j],nums[first]
                backtrack(first+1)
                nums[first],nums[j]=nums[j],nums[first]
        
        backtrack(0)
        return res
                
        
        
        
        
        
        
        def backtrack(i,output):
            if len(output)==n:
                res.append(output[:])
                return 
            for j in range(i,n):
                output.append(nums[i])
                backtrack(j+1,output)
                output.pop()
        
        backtrack(0,[])
        return res
       