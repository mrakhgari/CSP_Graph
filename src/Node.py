class Node:
    def __init__(self, id, shape):
        self.id = id
        self.index = 0
        self.adj = []
        self.shape = shape
        self.domain = list(range(1,10,1))
        self.reduces = {}

    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        # return str(self.id) + ' ' + str(self.shape)+ ' ' + str(self.index)
        return str(self.index) 

    def __repr__(self):
        return str(self)
    
    
    def __it__(self, other):
        print('===========================')
        return len(self.domain)< len(other.domain)

    def __cmp__(self, other):
        return len(self.domain) < len(other.domain)

    # def is_consistent(self, graph): # implement in sub calss 
    #     print('is_consistent' + str(self))
    #     # for adj in graph[self]:
    
    def add_reduce(self, node, domain):
        self.reduces[node] = domain
    
    def recover(self, graph):
        print('in recover')
        for adj in graph[self]:
            if self.reduces.get(adj) is not None:
                adj.domain.expend(self.reduces[adj])

    def set_domain(self):
        print('in set domain')

    
