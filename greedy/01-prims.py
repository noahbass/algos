# Prim's algorithm for finding a minimum spanning tree of a weighted, undirected graph
# 
# 
import math

# g: a connected graph with vertex set V and edge set E
# w: a weight function on E for the graph g
# r: vertex to start the spanning tree
# returns: a minimum spanning tree as a parent array
def prims(g, w, r):
    n = len(g) # length is the number of vertices in the graph
    parent = [-1] * n
    nearest = [math.inf] * n
    visited = [False] * n

    parent[r] = -1 # mark the root vertex r
    nearest[r] = 0

    for _ in range(1, n): # 1...n-1
        # Select vertex u that minimizes nearest[u] over all u such that visited[u] == False
        u = minNearest(nearest, visited)
        visited[u] = True # add u to the tree array

        for v in g[u]: # each arc from u to v
            # update nearest[v] and parent[v] for all v that
            # are adjacent to u and not already in the tree array
            if visited[v] == False:
                # v is not in tree array
                if w[(u, v)] < nearest[v]:
                    # the weight of u->v is less than v
                    nearest[v] = w[(u, v)]
                    parent[v] = u
                    # print(g[u], ': ', v)
        # print(nearest, visited)

    return parent

# Find the minimum item in the nearest array, but only for unvisited items
def minNearest(nearest, visited):
    min = math.inf
    min_index = 0

    for v in range(0, len(visited)):
        if nearest[v] < min and visited[v] == False: 
            min = nearest[v]
            min_index = v

    return min_index

if __name__ == "__main__":
    # adjacency list representation of the graph
    graph1 = {
        0: [1, 3],
        1: [0, 2, 3],
        2: [1, 3],
        3: [0, 1, 2]
    }
    # weights each edge of the graph
    weights1 = {
        (0, 3): 1,
        (0, 1): 4,
        (1, 3): 3,
        (3, 2): 5,
        (3, 1): 3,
        (1, 2): 6
    }

    parent_array1 = prims(graph1, weights1, 0)
    assert parent_array1 == [-1, 3, 3, 0]
    print(parent_array1)

    # adjacency list representation of the graph
    graph2 = {
        0: [1, 2, 5],
        1: [0, 2, 3],
        2: [0, 1, 3, 5],
        3: [1, 2, 4],
        4: [3, 5],
        5: [0, 2, 4]
    }
    # weights each edge of the graph
    weights2 = {
        (0, 1): 1,
        (0, 2): 9,
        (0, 5): 14,
        (1, 0): 1,
        (1, 2): 10,
        (1, 3): 15,
        (2, 0): 9,
        (2, 1): 10,
        (2, 3): 11,
        (2, 5): 2,
        (3, 1): 15,
        (3, 2): 11,
        (3, 4): 6,
        (4, 3): 6,
        (4, 5): 9,
        (5, 0): 14,
        (5, 2): 2,
        (5, 4): 9
    }

    parent_array2 = prims(graph2, weights2, 1)
    assert parent_array2 == [1, -1, 0, 4, 5, 2]
    print(parent_array2)
