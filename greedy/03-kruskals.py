# Kruskals's algorithm for finding a minimum spanning tree of a weighted,
# undirected graph. Kruskals's grows a minumum spanning tree by combining forests of trees.
# 
# Given a connected graph G = (V,E), with |V| = n and |E| = m, and a weight
# function w defined on the edge set E, Kruskal’s algorithm finds a minimum
# spanning tree T of G by constructing a sequence of n forests.


# g: a connected graph with vertex set V and edge set E
# w: a weight function on E for the graph g
# returns: a minimum spanning tree as a parent array
def kruskals(g, w):
    n = len(g)  # length is the number of vertices in the graph
    m = len(w)
    parent = [-1] * n  # an array representing disjoint sets
    forest = []

    # sort the edges by weight (smallest first) - θ(n log n)
    # ex: [(1, (0, 3)), (3, (1, 3)), (3, (3, 1))]
    edges_sorted = sorted((value, key) for (key, value) in w.items())

    size = 0
    j = 0
    while size <= n - 1 and j < m:
        j += 1
        edge = edges_sorted.pop(0)  # pop off the first item in array
        (u, v) = edge[1]  # use index 1 to get only the edge tuple, not the weight

        u_root = find(parent, u)
        v_root = find(parent, v)

        if u_root != v_root:
            # add the edge (u, v) to the forest
            size += 1
            forest += [(u, v)]
            union(parent, u_root, v_root)

    return forest


# Returns the parent of the vertex at i.
# Follows the chain of parent pointers from x up the tree until it reaches a root element, whose parent is itself.
def find(parent, i):
    if parent[i] < 0:
        return i
    return find(parent, parent[i])


# Returns the union of two disjoint sets (forests).
# The smaller forest (in tree height) is added to the larger forest.
def union(parent, u, v):
    sub_tree_sum = parent[u] + parent[v]

    if parent[u] > parent[v]:
        parent[u] = v
        parent[v] = sub_tree_sum
    else:
        parent[v] = u
        parent[u] = sub_tree_sum


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
        (1, 2): 6,
    }

    forest1 = kruskals(graph1, weights1)
    assert forest1 == [(0, 3), (1, 3), (3, 2)]
    print(forest1)

    # adjacency list representation of the graph
    graph2 = {
        0: [1, 5],
        1: [0, 5, 2],
        2: [1, 5, 4, 3],
        3: [4, 2],
        4: [5, 2, 3],
        5: [0, 1, 2, 4]
    }
    # weights each edge of the graph
    weights2 = {
        (0, 1): 4,
        (0, 5): 1,
        (1, 5): 3,
        (1, 2): 7,
        (2, 5): 11,
        (2, 4): 3,
        (2, 3): 5,
        (3, 4): 2,
        (4, 5): 6
    }

    forest2 = kruskals(graph2, weights2)
    assert forest2 == [(0, 5), (3, 4), (1, 5), (2, 4), (4, 5)]
    print(forest2)
