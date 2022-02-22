class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float("inf")
        sums=0
        
        def threesum(nums,i):
            j=i+1
            r=len(nums)-1
            d=float('inf')
            c=1
            while j<r:
                g=nums[i]+nums[j]+nums[r]
                current_diff=g-target
                if d>abs(current_diff):
                    d=abs(current_diff)
                    if current_diff<0:
                        c=-1
                    else:
                        c=1
                if current_diff <0:
                    j+=1
                elif current_diff>0:
                    r-=1
                else:
                    break
            return d,c
                
        for i in range(len(nums)):
            
            d,c=threesum(nums,i)
            if diff>d:
                diff=d
                sums=target + c*d
            if d==0:
                break
        
        return sums
        
        
        
        