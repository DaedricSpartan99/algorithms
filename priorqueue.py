from heap import Heap
import heap

class Priority_queue(Heap):
    def __init__(self, A):
        # build heap
        Heap.__init__(self, A)
    
    def insert(self, key):
        self.A.append(float('-inf'))
        self.increase_key(len(self)-1, key)
        return self

    def maximum(self):
        return self.A[0]

    def extract_max(self):
        if len(self) < 1:
            raise Exception("Heap underflow")

        out = self.maximum()
        n = len(self)-1
        self.A[0] = self.A[n]
        del self.A[n]
        self.heapify(0, n)
        return out

    def increase_key(self, i, key):
        if key < self.A[i]:
            raise Exception("New key is smaller than current one")

        self.A[i] = key
        p = heap.parnt(i)
        while i > 0 and self.A[p] < self.A[i]:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p = heap.parent(i)
        return self
