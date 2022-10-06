from collections import deque
class MyQueue(object):

    def __init__(self):
        self._values = deque()
        self._val = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._values.append(x)
        if len(self._val) == 0:
            while len(self._values) > 0:
                self._val.append(self._values.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self._values) == 0 and len(self._val) == 0:
            return None
        elif len(self._val) == 0:
            while len(self._values) > 0:
                self._val.append(self._values.pop())
        
        return self._val.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self._values) == 0 and len(self._val) == 0:
            return None
        elif len(self._val) == 0:
            while len(self._values) > 0:
                self._val.append(self._values.pop())
        
        peek = self._val.pop()
        self._val.append(peek)
        return peek
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._values) == 0 and len(self._val) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()