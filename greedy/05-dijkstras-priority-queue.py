# Dijkstra's algorithm (using a min priority queue -- a min-heap) for finding
# the shortest path *tree* of a graph for weighted graphs and digraphs given
# an initial vertex to start the search.
#
# Dijkstra's algorithm returns an array of the shortest distance from the
# initial vertex to all other vertexes as well as a minimum spanning tree.
#
# This implementation with a min-heap requires that all vertices are examined once.
#
# See 04-dijkstras.py for further information on the θ(||V|^2 solution)
#
# This algorithm runs in worst-case time θ(|E| + |V| log |V|)

import math
import heapq


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

    q = []  # a min-heap for storing the weighted edges
    heapq.heappush(q, (0, r))  # the initial vertex has weight 0

    parent[r] = -1
    dist[r] = 0

    while len(q) != 0:
        # select the vertex u that minimizes dist[u] over all u such that visited[u] is False
        (_, u) = heapq.heappop(q)
        visited[u] = True

        # examine the neighbors of u
        for v in g[u]:
            if visited[v] is False and (dist[u] + w[(u, v)]) < dist[v]:
                dist[v] = dist[u] + w[(u, v)]
                parent[v] = u
                heapq.heappush(q, (dist[v], v))

    return parent, dist


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
