class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue=deque([start])
        visited=set()
        while queue:
            curr=queue.popleft()
            visited.add(curr)
            if curr==end:
                return True
            for nodes in graph[curr]:
                if nodes not in visited:
                    queue.append(nodes)
        return False
       