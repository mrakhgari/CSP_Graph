from Node import Node
from Helper import backtracking_search, bt_mrv
import networkx as nx
import matplotlib.pyplot as plt

from Circle import Circle
from Hexagon import Hexagon
from Pentagon import Pentagon
from Square import Square
from Triangle import Triangle

shapes = {'C': 'o', 'P': 'p', 'H': 'H', 'S': 's', 'T': '^'}
G = nx.Graph()
vertices = []


def create_nodes(f):
    try:
        for (i, shape) in enumerate(f.readline().split()):
            if shape.upper() == 'C':
                vertices.append(Circle(i))
            elif shape.upper() == 'P':
                vertices.append(Pentagon(i))
            elif shape.upper() == 'H':
                vertices.append(Hexagon(i))
            elif shape.upper() == 'S':
                vertices.append(Square(i))
            elif shape.upper() == 'T':
                vertices.append(Triangle(i))
    except KeyError:
        print('invalid shape... please enter correct...')


def create_edges(f, E):
    for _ in range(E):
        src, des = map(int, f.readline().split())
        G.add_edge(vertices[src], vertices[des])


def create_graph():
    # _ is number of vertices and e is number of edges
    try:
        f = open("./input.txt", 'r')
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
    draw_graph(G)
    backtracking_search(G)
    draw_graph(G)


if __name__ == "__main__":
    main()
