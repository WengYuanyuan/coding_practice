class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.minItem = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minStack.append(x)
        if len(self.minItem) == 0 or x <= self.minItem[-1]:
            self.minItem.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.minStack) != 0:
            if len(self.minItem)!=0 and self.minStack[-1] == self.minItem[-1]:
                self.minItem = self.minItem[:-1]
            self.minStack = self.minStack[:-1]

        

    def top(self):
        """
        :rtype: int
        """
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minItem) == 0:
            return None
        return self.minItem[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()