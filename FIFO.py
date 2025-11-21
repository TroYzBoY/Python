from collections import deque


class Queue:
    def __init__(self):
        self._q = deque()

    def enqueue(self, x):
        self._q.append(x)  # O(1)

    def dequeue(self):
        return self._q.popleft()  # O(1)

    def is_empty(self):
        return not self._q


q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue())  # A