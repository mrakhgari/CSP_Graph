class Node:

    def __init__(self, shape):
        self.shape = shape
        self.domain = list(range(1, 10, 1))
        self.index = 0

    def __str__(self):
        return str(self.index) + str(self.shape) + str(self.domain)

    def __repr__(self):
        return str(self)

