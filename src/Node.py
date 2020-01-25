class Node:

    def __init__(self, shape):
        self.shape = shape
        self.domain = list(range(1, 10, 1))
        self.index = 0

    def __str__(self):
        return str(self.index) + str(self.shape) + str(self.domain)

    def __repr__(self):
        return str(self)

    #     pos = nx.spring_layout(g, scale=3)
    # nodes = list(g.nodes())
    # for i in nodes:
    #     nx.draw_networkx(g,pos, node_shape=i.shape, nodelist= [i], node_size=600)

    # nx.draw_networkx_edges(g,pos)
