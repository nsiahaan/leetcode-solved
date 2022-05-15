class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for i in s:
            if i in paren:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if i != paren[top]:
                    return False
        if len(stack) != 0:
            return False
        return True