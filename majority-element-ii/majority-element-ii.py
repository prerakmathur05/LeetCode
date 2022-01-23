class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        res=set()
        l=len(nums)
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
            if dic[num]> l/3:
                res.add(num)
        return res
        