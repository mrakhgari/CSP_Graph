from Node import Node


class Hexagon(Node):
    
    def __init__(self, id):
        super().__init__(id , 'H')

    def is_consistent(self, graph):
        res = 0
        for adj in graph[self]:
            if adj.index == 0:
                return True
            res += adj.index
        res %= 10
        if res == 0:
            return False
        return res == self.index

    def __cmp__(self, other):
        return super().__cmp__(other)

    def __it__(self, other):
        return super().__it__( other)
    # def remove_intercalary_domain(self, node_domain):
    #     sum_values = node_domain[self.adjacent_nodes[0]]
    #     for i in range(1, len(self.adjacent_nodes)):
    #         new_sum_values = []
    #         for v in sum_values:
    #             for q in node_domain[self.adjacent_nodes[i]]:
    #                 new_sum_values.append(v + q)
    #         sum_values = new_sum_values
    #     possible_value = set()
    #     for value in sum_values:
    #         possible_value.add(self.least_significant_value(value))

    #     possible_value = list(possible_value)
    #     node_domain[self] = [
    #         v for v in node_domain[self] if v in possible_value]
