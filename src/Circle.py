from Node import Node


class Circle(Node):
    
    def __init__(self, id):
        super().__init__(id , 'o')
    def is_consistent(self, graph):
        return True

        
    def __cmp__(self, other):
        return super().__cmp__(other)

    def __it__(self, other):
        return super().__it__( other)
    # def remove_intercalary_domain(self, node_domain):
    #     return 0