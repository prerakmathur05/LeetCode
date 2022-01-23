class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        sums=sum(nums)
        requiredsum=(n * (n+1))//2
        return requiredsum - sums
        
        