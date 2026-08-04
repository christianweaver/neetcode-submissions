class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        paren_dict = {"(": ")", "{": "}", "[": "]"}

        paren_stack = []

        for c in s:
            if c in paren_dict:
                paren_stack.append(c)
            else:
                if paren_stack and paren_dict[paren_stack.pop()] == c:
                    continue
                else:
                    return False
        
        return not paren_stack
