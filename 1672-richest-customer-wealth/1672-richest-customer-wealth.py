class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        cur=0
        hashmap={}
        for row in range(len(accounts)):
            for col in range(len(accounts[0])):
                if row in hashmap:
                    hashmap[row]+=accounts[row][col]
                else:
                    hashmap[row]=accounts[row][col]
        return max(hashmap.values())            
                
        