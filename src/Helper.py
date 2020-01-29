def backtracking_search(nodes):
    return bt(nodes)


def assigment_is_complete(graph):
    print('in the check complete')
    for node in graph.nodes():
        if node.index == 0:
            return False
    return True


def is_consistent_with(graph): # completed 
    for node in graph.nodes():
        print(type(node))
        if not node.is_consistent(graph):
            return False
    return True


def forward_checking(graph, node):
    for adj in graph[node]:
        if adj.index == 0:
            node.add_reduce(adj, adj.set_domain())  # need for recover


def remove_assignment_inferences(graph,node):
    node.recover(graph)


def bt(graph):
    if assigment_is_complete(graph):  # check completed or not ?
        return True
    var = [node for node in graph.nodes() if node.index ==
           0][0]  # unassigned variable

    for value in var.domain:
        var.index = value
        if is_consistent_with(graph):  # check that the result is true ?
            # change the reduces in the node class
            forward_checking(graph, var)
            if bt(graph):
                return True
            remove_assignment_inferences(graph, var)
    var.index = 0
    return False

def find_mrv(graph):
    min_d = 10
    for node in graph.nodes():
        if node.index == 0 :
            if len(node.domain)<min_d:
                min_d = len(node.domain)
                var = node
    return var

def bt_mrv(graph):
    
    if assigment_is_complete(graph):  # check completed or not ?
        return True
    # var = min([node for node in graph.nodes() if node.index ==
        #    0])  # unassigned variable
    var = find_mrv(graph)
    for value in var.domain:
        var.index = value
        if is_consistent_with(graph):  # check that the result is true ?
            # change the reduces in the node class
            forward_checking(graph, var)

            if bt(graph):
                return True
            remove_assignment_inferences(graph, var)
    var.index = 0
    return False
