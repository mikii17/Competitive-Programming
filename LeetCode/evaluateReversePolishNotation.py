from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "*":
                stack.append(stack.pop() * stack.pop())
            elif item == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif item == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))
            else:
                stack.append(int(item))
        
        return stack.pop()
