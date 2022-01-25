class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftproduct=[1]*n
        rightproduct=[1]*n
        
        
        for i in range(1,n):
            leftproduct[i]=leftproduct[i-1]*nums[i-1]
            rightproduct[n-i-1]=rightproduct[n-i]*nums[n-i]
        res=[1]*n
        for i in range(n):
            res[i]=leftproduct[i] * rightproduct[i]
        return res
        
        