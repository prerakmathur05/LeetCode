class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if num<10:
                continue
            r=num//10
            if r<10:
                count+=1
            elif r>= 10 and r<100:
                continue
            elif r>=100 and r<1000:
                count+=1
    
            elif r>=1000 and r<10000:
                continue
            elif r>=10000 and r<100000:
                count+=1
        return count
                