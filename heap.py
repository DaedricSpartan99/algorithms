#!/usr/bin/python


# vertical level on the tree
def levelof(i):
    return (i+1).bit_length() - 1

# horizonthal position on the specified index
def posof(i):
    return (i+1) - (1 << (levelof(i)))

# convert a level h and horizonthal position j into an index
def collapse(h,j):
    return 2**h + j - 1

# parent index
def parnt(i):
    return collapse(levelof(i)-1, posof(i) // 2)

def left(i):
    return collapse(levelof(i)+1, 2 * posof(i))

def right(i):
    return left(i) + 1

def parent(i):
    return (levelof(i) // 2) + (posof(i) // 2)


class Heap:
    def __init__(self, A, compare = lambda a,b: a > b, **kargs):
        self.A = A
        self.compare = compare
        builden = "build" in kargs
        if (builden and kargs["build"]) or not builden:    
            self.build_heap()

    
    def __len__(self):
        return len(self.A)

    def build_heap(self):
        n = len(self)
        for i in range(n//2-1, -1, -1):
            self.heapify(i, n)

    def heapify(self, i, stop = -1):
        n = stop

        #print("Analysing index: ", i)

        if n == -1:
            n = len(self)

        l = left(i)
        r = right(i)
        largest = i

        if l < n and self.compare(self.A[l], self.A[i]):
            largest = l

        if r < n and self.compare(self.A[r], self.A[largest]):
            largest = r

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.heapify(largest, n)
        return self

    def __str__(self):
        s = "("
        A = self.A
        N = len(self).bit_length()

        for i in range(N-1):
            m = (1 << i) - 1 # level begin
            s += '['

            for j in range(m):
                #print("i =", i, ", m + j =", m + j)
                s += '%s, ' % (A[m + j])

            s += '%s]' % (A[2 * m])
            s += '; '

        m = (1 << (N-1)) - 1
        s += '['
        for j in range(m, len(A)-1):
            s += '%s, ' % (A[j])
        s += '%s]' % (self.A[len(A)-1])
        s += ')'
        return s

def heapsort(A):
    H = Heap(A)
    H.build_heap()
    n = len(H) 
    for i in range(n-1, 0, -1):
        H.A[0], H.A[i] = H.A[i], H.A[0]
        H.heapify(0, i)
    return A
