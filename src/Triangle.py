from math import log10, floor
from Node import Node


class Triangle(Node):
    
    def __init__(self, id):
        super().__init__(id , '^')

    def is_consistent(self, graph):
        res = 1
        for adj in graph[self]:
            if adj.index == 0:
                return True
            res *= adj.index
        res = int(str(res)[:1])
        return res == self.index
    
    # def remove_intercalary_domain(self, node_domain):
    #     mul_values = node_domain[self.adjacent_nodes[0]]
    #     for i in range(1, len(self.adjacent_nodes)):
    #         new_mul_values = []
    #         for v in mul_values:
    #             for q in node_domain[self.adjacent_nodes[i]]:
    #                 new_mul_values.append(v * q)
    #         mul_values = new_mul_values
    #     possible_value = set()
    #     for value in mul_values:
    #         possible_value.add(self.most_significant_value(value))

    #     possible_value = list(possible_value)
    #     node_domain[self] = [v for v in node_domain[self] if v in possible_value]


    def __cmp__(self, other):
        return super().__cmp__(other)

    def __it__(self, other):
        return super().__it__( other)