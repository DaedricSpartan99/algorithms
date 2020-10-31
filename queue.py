
# out of bounds constant
npos = -1

# construct a Queue object from a generic buffer A
class Queue:
    def __init__(self, A, head = npos, tail = npos):
        if A is None:
            self.A = []
        else:
            self.A = A
        self.head = head

        if tail == npos:
            self.tail = head # reset
        else:
            self.tail = tail

    
    # check whether is enough capient
    # allocate n fields in A if necessary
    def resize_buffer(self, n):
        if (len(self.A) - self.tail) < n:
            self.A = self.A + [0] * n

    def length(self):
        return len(self.A)

    def enqueue(self, x):
        self.A[self.tail] = x

        if self.tail == self.length():
            self.tail = 0 # reset
        else:
            self.tail += 1

    def dequeue(self):
        x = self.A[self.head]

        if self.head == self.length():
            self.head = 0 # reset
        else:
            self.head += 1

        return x

    def front(self):
        if self.head == npos:
            return None
        else:
            return self.A[self.head]

    def back(self):
        if self.tail == self.head:
            return None
        else:
            return self.A[self.back-1]

