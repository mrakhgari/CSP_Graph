def set_domains(constraints, node):
    # for constraint in constraints:
    # if constraint
    pass
#


def backtrack(graph, constraints):
    for node in graph.nodes():
        if node.index == 0:
            while True:
                if len(node.get_domain()) == 0:
                    return False
                else:
                    candidate = node.get_domain().pop(0)
                    node.set_index(candidate)
                    if backtrack(graph, None):
                        return True
    return True
