import sys

class Queue:
    """
        Queue: FIFO Data Structure.
        Operations:
            enqueue(item)
            dequeue()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an empty queue.
            Here we are using list to implement the Queue data structure.
        """
        self._data = []

    def isEmpty(self):
        """
            Test if the queue has no items.
            :return: True if Queue is Empty. False Otherwise
        """
        return self.size() == 0

    def enqueue(self, item):
        """
            Insert the item at the rear of the Queue
            :param item: item to be added on to the Queue
        """
        self._data.append(item)

    def dequeue(self):
        """
            Removes an item from the front of the Queue.
            :return: item removed from the front of the Queue.
            :raises: EmptyQueueError if Queue has no elements.
        """
        if self.isEmpty():
            raise EmptyQueueError("Trying to dequeue from an Empty Queue.")

        return self._data.pop(0)

    def size(self):
        """
            Returns the number of elements currently in the Queue.
            :return: size of the Queue.
        """
        return len(self._data)



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

    def set_weight(self, to_vertex, weight):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                self._neighbors[self._neighbors.index(neighbor)] = (neighbor[0], weight)

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

    def bfs(self, source, target, path):
        source_vertex = self.get_vertex(source)

        # Initially none of the nodes are visited
        visited = [False] * len(self._vertices)

        # Since we are starting at source, mark it visited and push it onto the queue
        visited[source] = True
        q = Queue()
        q.enqueue(source_vertex)

        # We need to exhaust all the items in the queue to see if there is an augmented path
        # from source to target.
        while not q.isEmpty():
            current_vertex = q.dequeue()
            current_vertex_key = current_vertex.get_key()

            # For each of the edges(including reverse edges),
            # if the other end of the edge is not visited and has a positive flow
            # Mark it as visited and update the path to the node as the current vertex.
            for neighbor in current_vertex.get_connections():
                neighbor_vertex_key = neighbor[0].get_key()
                if not visited[neighbor_vertex_key] and neighbor[1] > 0:
                    q.enqueue(neighbor[0])

                    visited[neighbor_vertex_key] = True
                    path[neighbor_vertex_key] = current_vertex_key

                    # Along the way, if we reach the target, we have found an augmented path.
                    if neighbor_vertex_key == target:
                        return True

        # If the queue is exhausted, the no augmented path is available.
        return False

    def ford_fulkerson(self, source, target):
        # This list is passed to bfs which populates the path to each node traversed.
        path = [-1] * len(self._vertices)

        # Initialize max_flow to 0 as there is no flow yet.
        max_flow = 0

        # For all the augmented paths from source to target with a flow greater than 0
        while self.bfs(source, target, path):

            # Find minimum residual capacity of the edges along the path as suggested by BFS.
            path_flow = sys.maxsize
            s = target
            while (s != source):
                path_flow = min(path_flow, self.get_vertex(path[s]).get_weight(s))
                s = path[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges along the path
            v = target
            while (v != source):
                u = path[v]
                u_vertex = self.get_vertex(u)
                v_vertex = self.get_vertex(v)

                u_vertex.set_weight(v, u_vertex.get_weight(v) - path_flow)
                v_vertex.set_weight(u, v_vertex.get_weight(u) + path_flow)

                v = path[v]

            # Reset the path for next BFS.
            path = [-1] * len(self._vertices)

        return max_flow
