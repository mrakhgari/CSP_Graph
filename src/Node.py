class Node:

    def __init__(self, id, shape):
        self.id = id
        self.shape = shape
        self.domain = list(range(1, 10, 1))
        self.index = 0

    def __str__(self):
        # return str(self.id) + str(self.index) + str(self.shape) + str(self.domain)
        return str(self.index)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        print('in eq'+ str(other.id))
        return self.id == other.id

    def get_domain(self):
        return self.domain

    def __hash__(self):
        return hash(self.id)

    def set_index(self, index):
        print('in the set index method, old index was ' +
              str(self.index) + ' and new index is ' + str(index))
        self.index = index
