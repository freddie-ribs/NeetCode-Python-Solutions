class MinStack:
    '''
    Stack operations in O(1) time
    '''

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = self.getMin()
        if minimum == None or minimum > val:
            minimum = val
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
