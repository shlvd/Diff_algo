class Stack:
    """
        Stack: LIFO Data Structure.
        Operations:
            push(item)
            pop()
            peek()
            isEmpty()
            size()
    """

    def __init__(self):
        """
            Define an empty stack.
            Here we are using list to implement the Stack data structure.
        """
        self._list = []         #Hold items in the stack.
        self._top = -1          #Denotes the top of the stack

    def isEmpty(self):
        """
            Test if the stack has no items.
            :return: True if Stack is Empty. False Otherwise
        """
        return self._top == -1

    def push(self, item):
        """
            Pushes an item at the top of the stack updating the top of the stack.
            :param item: item to be added on to the stack
        """
        self._list.append(item)
        self._top += 1

    def pop(self):
        """
            Removes an item from the top of the stack modifying it.
            :return: item removed from the top of the stack.
            :raises: EmptyStackError if stack has no elements.
        """
        if self.isEmpty():
            raise EmptyStackError("Stack is Empty: Trying to pop from an empty stack")

        self._top -= 1
        return self._list.pop()

    def peek(self):
        """
            Just returns the item at the top of the stack without modifying the stack.
            :return: item at the top of the stack.
            :raises: EmptyStackError if stack has no elements.
        """
        if self.isEmpty():
            raise EmptyStackError("Stack is Empty: Trying to peek into an empty stack")

        return self._list[self._top]

    def size(self):
        """
            Returns the number of elements currently in the stack.
            :return: size of the stack.
        """
        return self._top + 1


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

    def BFS(self, start_vertex):
        start_vertex = self.get_vertex(start_vertex)

        if start_vertex is None:
            raise Exception("Vertex {} is not found in graph".format(start_vertex))

        visited = [False] * len(self._vertices)
        traversed = []

        q = Queue()
        q.enqueue(start_vertex)

        while not q.isEmpty():
            v = q.dequeue()
            key = v.get_key()

            if not visited[key]:
                visited[key] = True
                traversed.append(key)

                for neighbor in v.get_connections():
                    if not visited[neighbor[0].get_key()]:
                        q.enqueue(neighbor[0])

        return traversed

    def DFS(self, start_vertex):
        start_vertex = self.get_vertex(start_vertex)

        if start_vertex is None:
            raise Exception("Vertex {} is not found in graph".format(start_vertex))

        visited = [False] * len(self._vertices)
        traversed = []

        q = Stack()
        q.push(start_vertex)

        while not q.isEmpty():
            v = q.pop()
            key = v.get_key()

            if not visited[key]:
                visited[key] = True
                traversed.append(key)

                for neighbor in v.get_connections():
                    if not visited[neighbor[0].get_key()]:
                        q.push(neighbor[0])

        return traversed
