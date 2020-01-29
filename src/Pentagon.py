from Node import Node
import itertools


class Pentagon(Node):
    def __init__(self, id):
        super().__init__(id , 'p')

    def is_consistent(self, graph):
        print('in pantagon')
        res = 0
        for adj in graph[self]:
            if adj.index == 0:
                return True
            res += adj.index
        res = int(str(res)[:1])
        return res == self.index

    # def set_domain(graph):
        # pass
        # l = []
        # new_domain = []
        # for adj in graph[node]:
        #     l.append(adj)
        # for element in itertools.product(l):
        #     print(element)
        #     if self.index = int(str(sum(element)[:1])):
        #         new_domain.append(element)
        # for elem in new_domain:

    def __cmp__(self, other):
        return super().__cmp__(other)

    def __it__(self, other):
        print('h')
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
    #         possible_value.add(self.most_significant_value(value))

    #     possible_value = list(possible_value)
    #     node_domain[self] = [
    #         v for v in node_domain[self] if v in possible_value]
