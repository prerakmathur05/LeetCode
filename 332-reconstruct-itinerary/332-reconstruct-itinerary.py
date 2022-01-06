class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        visited=defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
            graph[u].sort()
            visited[u].append(False)
        #print(graph)
        #print(visited)
        flights=len(tickets)
        results=[]
        route=["JFK"]
        def backtrack(node, route):
            #print(route)
            if len(route) == flights+1:
                #print("If called")
                results.extend(route)
                #print(results)
                return True
            for i, dest in enumerate(graph[node]):
                if not visited[node][i]:
                    visited[node][i]=True
                    r=backtrack(dest, route + [dest])
                    visited[node][i]=False
                    if r:
                        return True
            return False
        
        backtrack("JFK",route)
        print(f"hrtd {results}")
        return results
    
            
            
            
            
        
        
        
        
        
        
        
        
        
        #below code will not work if you are tarvelling to destination twice pr more 
        graph=defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
        
        graph2=defaultdict(list)
        for u,v in tickets:
            graph2[v].append(u)
        
        start=dest=""
        print(graph)
        print(graph2)
        for i in graph:
            if len(graph[i]) > len(graph2[i]):
                start=i
        for i in graph2:
            if len(graph[i]) < len(graph2[i]):
                dest=i
        print(start)  
        print(dest)
            
        path=[]
        def dfs(node, path):
            path.append(node)
            if node==dest:
                return True
            for nodes in graph[node]:
                if dfs(nodes,path):
                    return True
            path.pop()
        
        dfs(start,path)
        return path
            
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        graph=defaultdict(list)
        for u,v in tickets:
            graph[u][0].append(v) #first list represent the destinations went froom u
            graph[v][1].append(u) #this represents the sources from you reached v
        start=""
        end=""
        for i in graph:
            if len(i[0])>len(i[1]):
                start=i
            elif len(i[0])<len(i[1]):
                end=i
        print(start)
        print(end)
        
                
            
            
        
        