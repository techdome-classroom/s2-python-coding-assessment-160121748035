class Solution(object):
    def isValid(self, s):
        def opposite(s):
            if s==')':
                return '('
            if s=='}':
                return '{'
            return '['
        stack , n = [] , 0
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
                n+=1
            else:
                if n>0:
                    if stack[n-1] == opposite(i):
                        stack.pop()
                        n-=1
                    else:
                        break
                else:
                    n = 1
                    break
        if n!=0:
            return False
        return True







    



  

