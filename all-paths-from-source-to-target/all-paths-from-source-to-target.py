class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
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
                        