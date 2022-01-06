class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        l=len(edges)
        root=[i for i in range(n)]
        rank=[1 for i in range(n)]
        def find(x):
            return root[x]
        def union(x,y):
            rootX=find(x)
            rootY=find(y)
            if rootX==rootY:
                return False
            else:
                if rank[rootX]>rank[rootY]:
                    root[rootY]=rootX
                    for i in range(n):
                        if root[i]==rootY:
                            root[i]=rootX
                elif rank[rootX]< rank[rootY]:
                    root[rootX]=rootY
                    for i in range(n):
                        if root[i]==rootX:
                            root[i]=rootY
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                    for i in range(n):
                        if root[i]==rootY:
                            root[i]=rootX
                return True
        for i in edges:
            k=union(i[0],i[1])
            if k==False:
                return False
        print(root)   
        print(rank)
        main=root[0]
        for i in root:
            if i!=main:
                return False
            
        return True
                

        
        
        
        
