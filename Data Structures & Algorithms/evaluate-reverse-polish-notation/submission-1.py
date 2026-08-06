class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for c in tokens:
            if c == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 + num2)
            elif c == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif c == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 / num2)
            elif c == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 * num2)
            else:
                stack.append(c)
        
        return int(stack.pop())