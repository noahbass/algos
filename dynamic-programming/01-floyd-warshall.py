# Floyd-Warshall's algorithm for finding the shortest path *tree* of a graph for
# weighted graphs and digraphs. This algorithm can be used on graphs that have
# negative weights (unlike Dijkstra's), but doesn't work with graphs with negative
# cycles (sum of the weights of the edges in the cycle is negative).
#
# θ(n^3)
#
# Floyd's takes as input the weight matrix for the graph (0 for a vertex to itself,
# infinity for a vertex that doesn't connect) and returns as output with the shortest
# paths and another matrix with the weight of the shortest paths from all vertices to
# all other vertices in the graph.

import math


# g: a connected digraph with vertex set V and edge set E (matrix representation of weights)
def floyds(g):
    n = len(g)

    # initialize the return matrices
    p = [[-1 for _ in range(n)] for _ in range(n)]  # weights of the shortest paths
    s = [[g[i][j] for j in range(n)] for i in range(n)]  # shortest path from any vertex to any other vertex

    for k in range(0, n):  # 0...n-1
        # print('stage:', k)
        # print_matrix(s)
        # print_matrix(p)
        for i in range(0, n):
            for j in range(0, n):
                if s[i][j] > s[i][k] + s[k][j]:
                    # a shorter path through vertex k exists, update p and s matrices
                    p[i][j] = k
                    s[i][j] = s[i][k] + s[k][j]

    return s, p


# pretty print a matrix
def print_matrix(matrix):
    print('[')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    print(']')


if __name__ == "__main__":
    # matrix representation of the digraph
    graph1 = [
        [0, 4, math.inf, 3, math.inf],
        [math.inf, 0, 6, math.inf, 2],
        [1, math.inf, 0, math.inf, math.inf],
        [4, math.inf, 2, 0, 3],
        [math.inf, math.inf, 1, math.inf, 0]
    ]

    # get the shortest path matrix and distances matrix
    shortest_paths1, distances1 = floyds(graph1)
    assert shortest_paths1 == [[0, 4, 5, 3, 6], [4, 0, 3, 7, 2], [1, 5, 0, 4, 7], [3, 7, 2, 0, 3], [2, 6, 1, 5, 0]]
    assert distances1 == [[-1, -1, 3, -1, 1], [4, -1, 4, 4, -1], [-1, 0, -1, 0, 1], [2, 2, -1, -1, -1], [2, 2, -1, 2, -1]]

    # matrix representation of the digraph
    graph2 = [
        [0, 9, math.inf, math.inf, math.inf, 1, math.inf],
        [9, 0, 1, math.inf, math.inf, 8, 2],
        [math.inf, 1, 0, 10, 1, math.inf, 2],
        [math.inf, math.inf, 10, 0, 4, math.inf, math.inf],
        [math.inf, math.inf, 1, 4, 0, 6, math.inf],
        [1, 8, math.inf, math.inf, 6, 0, 4],
        [math.inf, 2, 2, math.inf, math.inf, 4, 0]
    ]

    # get the shortest path matrix and distances matrix
    shortest_paths2, distances2 = floyds(graph2)
    assert shortest_paths2 == [[0, 7, 7, 11, 7, 1, 5], [7, 0, 1, 6, 2, 6, 2], [7, 1, 0, 5, 1, 6, 2], [11, 6, 5, 0, 4, 10, 7], [7, 2, 1, 4, 0, 6, 3], [1, 6, 6, 10, 6, 0, 4], [5, 2, 2, 7, 3, 4, 0]]
    assert distances2 == [[-1, 6, 6, 5, 5, -1, 5], [6, -1, -1, 4, 2, 6, -1], [6, -1, -1, 4, -1, 6, -1], [5, 4, 4, -1, -1, 4, 4], [5, 2, -1, -1, -1, -1, 2], [-1, 6, 6, 4, -1, -1, -1], [5, -1, -1, 4, 2, -1, -1]]

    # matrix representation of the digraph
    graph3 = [
        [0, math.inf, -2, math.inf, math.inf, math.inf],
        [3, 0, math.inf, math.inf, math.inf, math.inf],
        [math.inf, 4, 0, math.inf, 1, 3],
        [math.inf, math.inf, -1, 0, 1, math.inf],
        [math.inf, math.inf, math.inf, 2, 0, 1],
        [4, math.inf, 4, math.inf, math.inf, 0]
    ]

    # get the shortest path matrix and distances matrix
    shortest_paths3, distances3 = floyds(graph3)
    assert shortest_paths3 == [[0, 2, -2, 1, -1, 0], [3, 0, 1, 4, 2, 3], [6, 4, 0, 3, 1, 2], [5, 3, -1, 0, 0, 1], [5, 5, 1, 2, 0, 1], [4, 6, 2, 5, 3, 0]]
    assert distances3 == [[-1, 2, -1, 4, 2, 4], [-1, -1, 0, 4, 2, 4], [5, -1, -1, 4, -1, 4], [5, 2, -1, -1, 2, 4], [5, 3, 3, -1, -1, -1], [-1, 2, 0, 4, 2, -1]]
