class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                res = op1 + op2
                stack.append(res)
            elif token == '-':
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                res = op1 - op2
                stack.append(res)
            elif token == '*':
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                res = op1 * op2
                stack.append(res)
            elif token == '/':
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                print("op1:", op1)
                print("op2:", op2)
                res = int(op1 / op2)
                stack.append(res)
            else:
                intVal = int(token)
                print(intVal)
                stack.append(intVal)
        return stack[0]
        