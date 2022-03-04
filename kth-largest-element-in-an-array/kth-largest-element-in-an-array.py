class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=[-1 * i for i in nums]
        heapq.heapify(a)
        if k> len(a):
            return None
        res=0
        for i  in range(k):
            res=heapq.heappop(a)
        return res * -1
        
        