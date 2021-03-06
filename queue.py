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
