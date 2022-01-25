class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftproduct=[1]*n
        leftproduct[0]=nums[0]
        rightproduct=[1]*n
        rightproduct[n-1]=nums[-1]
        
        
        for i in range(1,n):
            leftproduct[i]=leftproduct[i-1]*nums[i]
            rightproduct[n-i-1]=rightproduct[n-i]*nums[n-i-1]
        print(leftproduct)
        print(rightproduct)
        res=[1]*n
        res[0]=rightproduct[1]
        res[n-1]=leftproduct[n-2]
        
        for i in range(1,n-1):
            res[i]=leftproduct[i-1] * rightproduct[i+1]
        return res
        
        