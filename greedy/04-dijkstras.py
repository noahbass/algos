# Dijkstra's algorithm for finding the shortest path *tree* of a graph for
# weighted graphs and digraphs given a initial vertex to start the search.
#
# Note that Dijkstra’s algorithm can't be used when a graph has edges with
# negative weights.
#
# Dijkstra’s algorithm is greedy. In each step (there are |V| steps), the algorithm
# minimizes the cost of the edges of reaching the next vertex from the initial vertex
# examined. In other words, at each step, we select an edge of minimum weight so that
# the path is the shortest path.
#
# This algorithm runs in worst-case time θ(|V|^2). An alternative algorithm that
# runs in worst-case time θ(|E| + |V| log |V|) is shown in `05-dijkstras-priority-queue.py`.

import math

# g: a connected graph with vertex set V and edge set E
# w: an edge set E with weights
# r: a vertex of g to begin finding the shortest path
# returns: a minimum spanning tree as a parent array and
#          the weights of shortest paths from r to each vertex
def dijkstras(g, w, r):
    n = len(g)  # length is the number of vertices in the graph
    parent = [-1] * n  # an array representing disjoint sets and the shortest path of the spanning tree
    dist = [math.inf] * n  # an array of weights of the shortest path from r to a vertex v
    visited = [False] * n

    # mark the initial vertex as root with weight 0
    parent[r] = -1
    dist[r] = 0

    for _ in range(1, n):
        # select the vertex u that minimizes dist[u] over all u such that visited[u] is False
        u = find(dist, visited)
        visited[u] = True

        # examine the neighbors of u
        for v in g[u]:
            if visited[v] is False and (dist[u] + w[(u, v)]) < dist[v]:
                dist[v] = dist[u] + w[(u, v)]
                parent[v] = u

    return parent, dist


# Return the minimally weighted unvisited vertex
def find(dist, visited):
    min_distance = math.inf
    min_index = 0

    for v in range(0, len(visited)):
        if visited[v] is False and dist[v] < min_distance:
            min_distance = dist[v]
            min_index = v

    return min_index


if __name__ == "__main__":
    # adjacency list representation of the *graph*
    graph1 = {
        0: [1, 3],
        1: [0, 2, 3],
        2: [1, 3],
        3: [0, 1, 2]
    }
    # weights each edge of the graph
    weights1 = {
        (0, 3): 1,
        (3, 0): 1,
        (0, 1): 4,
        (1, 0): 4,
        (1, 3): 3,
        (3, 1): 3,
        (3, 2): 5,
        (2, 3): 5,
        (1, 2): 6,
        (2, 1): 6
    }

    parent_array1, distance_array1 = dijkstras(graph1, weights1, 0)
    assert parent_array1 == [-1, 0, 3, 0]
    assert distance_array1 == [0, 4, 6, 1]
    print('parent:', parent_array1, '-- distance:', distance_array1)

    # adjacency list representation of the *digraph* (directed graph)
    graph2 = {
        0: [1, 5],
        1: [2, 5],
        2: [1, 3],
        3: [],
        4: [2, 3],
        5: [4, 2]
    }
    # weights each edge of the digraph
    weights2 = {
        (0, 1): 13,
        (0, 5): 1,
        (1, 5): 2,
        (1, 2): 1,
        (2, 1): 3,
        (2, 3): 6,
        (4, 3): 10,
        (4, 2): 3,
        (5, 2): 9,
        (5, 4): 4
    }

    parent_array2, distance_array2 = dijkstras(graph2, weights2, 0)
    assert parent_array2 == [-1, 2, 4, 2, 5, 0]
    assert distance_array2 == [0, 11, 8, 14, 5, 1]
    print('parent:', parent_array2, '-- distance:', distance_array2)
