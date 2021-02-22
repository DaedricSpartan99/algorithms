#!/usr/bin/python

import queue  # from custom class

# G = antisymmetric matrix representing links and capacities
class Flow:
    def __init__(self, G):
        self.G = G
        self.N = len(G)
        self.s = 0
        self.t = N-1 
    
    # apply bfs from source to sink using current state G
    def bfs(self, F, parents):
        Q = LinkedQueue()
        Q.enqueue(0)
        visited = [False for v in self.V] # visited state
        visited[0] = True

        while len(Q) > 0:
            u = Q.dequeue()

            for v in range(N):
                if not visited[v] and ((G[u][v] > 0 and F[u][v] >= 0 and F[u][v] < G[u][v]) or ((G[u][v] < 0 and F[u][v] <= 0 and F[u][v] > G[u][v])):
                    Q.enqueue(v)
                    visited[v] = True
                    parents[v] = u
        
        return visited[-1]

    def max_flow(self):
        f = 0 # flow value

        complzero = lambda i,j,A: 0 if A[i][j] >= 0 else A[i][j]

        # F is a complementary matrix (w.r.t self.G)
        F = [[complzero(v, u, self.G) for u in range(N)] for v in range(N)]
        
        # -1 = no parent
        parents = [-1 for v in self.V]

        while self.bst(F, parents):

            # reconstruct reverse path
            s = 0
            it = self.t
            revpath = LinkedQueue() 
            revpath.enqueue(it)

            cflow = float('inf')
            
            # notice the sink is enqueued, the source not
            while it != s:
                old = it
                it = parents[it]
                revpath.enqueue(it)
                if self.G[it][old] > 0:
                    cflow = min(cflow, self.G[it][old] - F[it][old])

            f += cflow
            
            # update f matrix
            it = 0
            while not revpath.empty():
                nit = revpath.dequeue() # next iterator
                F[it][nit] += cflow
        
        # output total
        return f 


