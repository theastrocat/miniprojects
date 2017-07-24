"""
Common search algorithms.
"""

def breadthfirst(graph,start, end):
    """
    Breadth First Search Algorithm.
    Returns shortest path and path taken as tuple.
    -------------------------------------
    Inputs:
        graph : Dictionary of connecting nodes
        start : Integer starting point on the graph
        end   : Integer ending point on the graph
    Outputs:
        path  : List of shortest path
        taken : List of the nodes checked in order
    """
    queue = []
    queue.append([start])
    taken = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        taken.append(node)
        if node == end:
            return path, taken
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def depthfirst(graph, start, end):
    """
    Depth First Search algorithm,
    Returns path taken and shortest path
    -----------------------------
    Inputs:
        graph : Dictionary of connecting nodes
        start : Integer starting point on the graph
        end   : Integer ending point on the graph
    Outputs:
        tpath : Path taken
        path  : Shortest path
    """
    path_queue = []
    path_queue.append([start])
    tpath = []
    while path_queue:
        path = path_queue.pop(0)
        #print path
        node = path[-1]
        tpath.append(node)
        if node == end:
            return tpath, path
        for adjacent in graph.get(node, [])[::-1]:
            new_path = path + [adjacent]
            path_queue = [new_path] + path_queue

def depthfirstright(graph, start, end):
    """
    Depth First Search algorithm,
    returns path takend so far...
    -----------------------------
    Inputs:
        graph : Dictionary of connecting nodes
        start : Integer starting point on the graph
        end   : Integer ending point on the graph
    Outputs:
        tpath  : Path taken
    """
    queue = []
    queue.append(start)
    tpath = []
    while queue:
        node = queue.pop(-1)
        tpath.append(node)
        newnodes = graph.get(node, [])
        if node == end:
            return tpath
        queue.extend(newnodes)
