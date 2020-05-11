class UnionFind:
    def __init__(self, n):
        self._n = n
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]

    # Returns representative of the set with element x
    def find(self, x):

        # if x is not the parent of itelf
        if(x != self._parent[x]):
            # We recursively find the parent of x.
            # And at each step back we optmize the data structure to hold
            # each node along the path under the representative.
            self._parent[x] = self.find(self._parent[x])

        return self._parent[x]

    def union(self, x, y):
        # Find the root of x and y
        (x_root, y_root) = (self.find(x), self.find(y))

        # If the are part of same set, they are already connected.
        if x_root == y_root:
            return

        # Move the node with lesser rank under the node with higher rank.
        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        elif self._rank[y_root] < self._rank[x_root]:
            self._parent[y_root] = x_root
        else:
            # If the rank is same, pick one representative and increment its rank.
            self._parent[y_root] = x_root
            self._rank[x_root] += 1

    def __str__(self):
        return str(self._parent)


class Vertex:
    """
    An example implementation of a Vertex or Node of a graph.
    """
    def __init__(self, key):
        """
        Creates a new Vertex.
        """
        self._neighbors = []
        self._key = key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                return neighbor[1]


class Graph:
    """
    An example implementation of Directed Graph ADT.
    """
    def __init__(self):
        """
        Creates a new, empty Graph.
        """
        self._vertices = {}

    def add_vertex(self, vertex):
        """
        Adds a new vertex into the graph.
        :param vertex: The Vertex to be added into the Graph.
        :return: None.
        """
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        """
        Add a directed edge between two vertices
        :param from_vertex: Starting vertex of the edge
        :param to_vertex: Where the edge ends.
        :param weight: weight of the edge
        :return: None
        """
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        """
        Get all the vertices of the directed Graph.
        :return: List of vertices of the graph.
        """
        vertices = self._vertices.keys()
        vertices.sort()
        return vertices

    def get_edges(self):
        """
        Get all the edges of the directed graph.
        :return: List of edges of the graph.
        """
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor[0].get_key())))

        return edges

    def get_vertex(self, vertex_key):
        for vertex in self._vertices:
            if vertex == vertex_key:
                return self._vertices[vertex]

        return None

    def kruskals(self):
        # Placeholder for the resulting minimum spanning tree
        result = []

        # Initialize the union-find data structure with an initial state
        # of all vertices being in distinct disjoint sets..
        no_of_vertices = len(self._vertices)
        uf = UnionFind(no_of_vertices)

        # Sort the edges in increasing order based on the weight.
        edges = sorted(self.get_edges(), key=lambda x: x[2])

        # Choose one edge at a time from the sorted list of edges.
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]

            # Check if the vertices of the edge are in same disjoint set.
            # If not, call an union, merge them to the same disjoint set.
            # Add the edge to result.
            if uf.find(vertex1) != uf.find(vertex2):
                uf.union(vertex1, vertex2)

                result.append(edge)

            # Optimize the algorithm by stopping when the number of edges
            # in result is n - 1.
            if len(result) == no_of_vertices - 1:
                break

        # Return the resulting minimum spanning tree.
        return result
