class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
                if i.isdigit() or i.startswith('-') and i[1:].isdigit():
                    stack.append(int(i))
                else:
                    right = stack.pop()
                    left = stack.pop()
                    if i == "+":
                        stack.append(left + right)
                    elif i == "-":
                        stack.append(left - right)
                    elif i == "*":
                        stack.append(left * right)
                    else: 
                        stack.append(int(left / right))

        return stack[0]