class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minimum_val[-1]) if self.minimum_val else val
        self.minimum_val.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minimum_val.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minimum_val[-1]
        
