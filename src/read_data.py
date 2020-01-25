from Node import Node
import networkx as nx
import matplotlib.pyplot as plt

shapes = {'C': 'o', 'P': 'p', 'H': 'H', 'S': 's', 'T': '^'}
G = nx.Graph()
vertices = []


def create_nodes(f):
    try:
        for shape in f.readline().split():
            vertices.append(Node(shapes[shape.upper()]))
    except KeyError:
        print('invalid shape... please enter correct...')


def create_edges(f, E):
    for _ in range(E):
        src, des = map(int, f.readline().split())
        G.add_edge(vertices[src], vertices[des])


def create_graph():
    # _ is number of vertices and e is number of edges
    try:
        f = open("./../input.txt", 'r')
    except OSError as e:
        print(e.strerror)
        exit(-1)
    _, E = map(int, f.readline().split())
    create_nodes(f)
    create_edges(f, E)
    f.close()


def draw_graph(g):
    pos = nx.spring_layout(g, scale=3)
    nodes = list(g.nodes())
    for i in nodes:
        nx.draw_networkx(g, pos, node_shape=i.shape,
                         nodelist=[i], node_size=700)

    nx.draw_networkx_edges(g, pos)
    plt.show()


def main():
    create_graph()
    print(G.nodes())
    draw_graph(G)


if __name__ == "__main__":
    main()
