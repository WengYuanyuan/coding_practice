class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.stream = []
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.stream.append(val)
        if len(self.stream) >= self.size:
            return sum(self.stream[-self.size:])/float(self.size)
        else:
            return sum(self.stream)/float(len(self.stream))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)