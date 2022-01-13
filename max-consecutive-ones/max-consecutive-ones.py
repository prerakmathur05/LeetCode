class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr=0
        maxi=float("-inf")
        for i in nums:
            if i==1:
                curr+=1
                maxi=max(curr,maxi)
            else:
                curr=0
        return maxi if maxi!=float("-inf") else 0
              