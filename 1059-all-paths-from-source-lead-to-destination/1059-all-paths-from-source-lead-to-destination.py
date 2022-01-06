class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # color w- not processed, g-under process and b=processed
        states=["w"]*n
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
        
        def dfs(node, states):
            if states[node]!="w":
                return states[node]=="b"
            if len(graph[node])==0:
                return node==destination
            states[node]="g"
            
            for dest in graph[node]:
                if not dfs(dest, states):
                    return False
                states[dest]="b"
            return True
        return dfs(source, states)
            
        
        
        
        
        
        
       # why below code fails is because we are masking a node visited and not visited, we are not taking into accout are we processing that node or not, or is there is any cycle i=through the processing node or not 
        graph=defaultdict(list)       
        for u,v in edges:
            graph[u].append(v)
        visited=set()    
        lastnode=destination
        def dfs(node):
            visited.add(node)
            print(node)
            if len(graph[node])==0:
                if node==destination:
                    visited.remove(node)
                return node==destination
            for nodes in graph[node]:
                if nodes in visited:   
                    return False
                else:
                    if not dfs(nodes):
                        return False
            return True
        return dfs(source)
                    