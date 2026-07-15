class MinStack(object):

    def __init__(self):
        self.minElems = []
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack or val <= self.minElems[-1]:
            self.minElems.append(val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.minElems[-1]:
            self.minElems.pop()
        

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minElems[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()