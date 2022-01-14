class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]= 0
        for i in range(k+1):
            tempPrices=prices[:]
            for s,d,c in flights:
                if prices[s]==float("inf"):
                    continue
                tempPrices[d]=min(tempPrices[d], prices[s]+c)
            prices=tempPrices
        

        return -1 if prices[dst]==float("inf") else prices[dst]
       
        
        
        