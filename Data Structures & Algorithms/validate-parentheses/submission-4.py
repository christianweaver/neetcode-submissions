class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {')': '(', '}': '{', ']': '['}
        stk =[]

        for c in s:
            if c not in paren_dict:
                stk.append(c)
            else:
                if not stk or paren_dict[c] != stk.pop():
                    return False
        
        return not stk