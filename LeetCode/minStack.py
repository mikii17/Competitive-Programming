class MinStack:

    def __init__(self):
        self._values = []
        self._minVal = []

    def push(self, val: int) -> None:
        self._values.append(val)
        if self._minVal:
            if self._minVal[-1] >= val:
                self._minVal.append(val)
        else:
            self._minVal.append(val)

    def pop(self) -> None:
        if len(self._values) == 0:
            return None
        if self._values[-1] == self._minVal[-1]:
            self._minVal.pop()
        
        return self._values.pop()

    def top(self) -> int:
        if len(self._values) == 0:
            return None
        return self._values[-1]

    def getMin(self) -> int:
        return self._minVal[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()