class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(set)
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
        maxi=0
        
        for i in range(n):
            for j in range(i):
                curr=len(graph[i])+len(graph[j])
                if j in graph[i]:
                    curr-=1
                maxi=max(curr,maxi)
        return maxi
        