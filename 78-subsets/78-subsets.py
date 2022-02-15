class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        res=[]
        def backtrack(i, output):
            if len(output) == k:
            #we have to return deep copy bcoz if output changes later then                  appended values in res will also change    
                res.append(output[:])  
                return
            for j in range(i, n):
                # add nums[j] into the current combination
                output.append(nums[j])
                # use next integers to complete the combination
                backtrack(j + 1, output)
                # backtrack
                output.pop()
        
        n = len(nums)
        for k in range(n + 1):
            backtrack(0,output)
        return res
        