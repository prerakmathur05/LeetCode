class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start=0
        end=len(graph)-1
        path=[start]
        queue=deque([path])
        res=[]
        while queue:
            curr=queue.popleft()
            node=curr[-1]
            for child in graph[node]:
                if child==end:
                    temp=curr[:]
                    temp.append(child)
                    res.append(temp[:])
                else:
                    temp=curr[:]
                    temp.append(child)
                    queue.append(temp)
            
        return res
            
        
        
        
        start=0
        end=len(graph)-1
        res=[]
        path=[]
        def backtrack(node,path):
            path.append(node)
            if node==end:
                res.append(path[:])
                return 
            for child in graph[node]:
                backtrack(child,path)
                path.pop()
                
        backtrack(0,path)
        return res
        
        #its given that its a directed acyclic graph so we really don't need to worry about cycles otherwise
        #we would be stuck in a loop forever
        target=len(graph)-1
        res=[]
        output=[]
        def dfs(node,output):
            output.append(node)
            if node==target:
                res.append(output[:])
                return 
            for childnode in graph[node]:
                dfs(childnode,output)
                
                output.pop()
                
        dfs(0,output)
        return res
                        