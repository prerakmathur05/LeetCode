class Solution:
    def simplifyPath(self, path: str) -> str:
        res=path.split("/")
        stack=[]
        for r in range(len(res)):
            if res[r]=="":
                continue
            elif res[r]==".":
                continue
            elif res[r]=="..":
                if stack:
                    stack.pop()
                
            else:
                stack.append(res[r])
        if not stack:
            return "/"
        print(stack)
        o="/".join(stack)
        return "/"+o        
                
                
                
                
            