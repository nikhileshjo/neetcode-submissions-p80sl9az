class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.stack_min = val
            return
        self.stack.append(val - self.stack_min)
        if val < self.stack_min:
            self.stack_min = val

    def pop(self) -> None:
        if not self.stack:
            return
        p_val = self.stack.pop()
        if p_val < 0:
            self.stack_min -= p_val        

    def top(self) -> int:
        if not self.stack:
            return
        t_val = self.stack[-1]
        if t_val < 0:
            return self.stack_min
        else:
            return t_val + self.stack_min
        

    def getMin(self) -> int:
        return self.stack_min
