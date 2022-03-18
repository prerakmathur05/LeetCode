class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={")":"(", "}":"{","]":"["}
        for char in s:
            if char in hashmap:
                c=stack.pop() if stack else "n"
                if hashmap[char]!=c:
                    return False
            else:
                stack.append(char)
        
        return not stack