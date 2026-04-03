class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for i in tokens:
            if i in ('+', '-', '*', '/'):
                right = num_stack.pop()
                left = num_stack.pop()
                if i == '+':
                    num_stack.append(left+right)
                elif i == '-':
                    num_stack.append(left-right)
                elif i == '*':
                    num_stack.append(left*right)
                else:
                    num_stack.append(int(left/right))
            else:
                num_stack.append(int(i))
        return num_stack.pop()