class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize: # check if maxsize, valid -> append x, else do nothing
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack: # if empty, return -1
            return -1
        else:
            top = self.stack[-1]
            del self.stack[-1] # remove (pop) last value
            return top

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < len(self.stack): # for k elements in range of stack
            self.stack[i] += val # increment by val
            i += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)