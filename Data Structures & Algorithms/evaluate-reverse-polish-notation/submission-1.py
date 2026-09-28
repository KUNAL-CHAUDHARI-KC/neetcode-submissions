class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        result = 0
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                 stack.append(int(tokens[i])) 
            else:
                operand = tokens[i]
                first = stack[-2] 
                second = stack[-1]

                if operand == "+":
                    result = first + second
                elif operand == "-":
                    result = first - second
                elif operand == "*":
                    result = first * second
                elif operand == "/":
                    result = int(first / second)
                
                stack.pop()
                stack.pop()

                stack.append(result)
        
        return stack[-1]
                

        