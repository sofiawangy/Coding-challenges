class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)