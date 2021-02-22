#!/usr/bin/python

# V = nodes, containing capacities
# V[0] = source 
# V[-1] = sink
# E = links, array containing indexes of edges in V and capacities (index, capacity)
class Flow:
    def __init__(self, V, E):
        self.V = V
        self.s = V[0]
        self.E = E
        self.t = V[-1]
    
    # apply bfs from source to sink using current state G
    def bfs(self, G, parents):
        Q = []
        Q.append(0)
        visited = [False for v in self.V] # visited state
        visited[0] = True

        while len(Q) > 0:
            u = Q[0]
            del Q[0] # dequeue
            for (v, flow, capacity) in G[u]:
                # TODO, allow backwards visiting with flow reduction
                if not visited[v] and flow < capacity:
                    Q.append(v)
                    visited[v] = True
                    parents[v] = u
        
        return visited[-1]

    def max_flow(self):
        f = 0 # flow value
        N = len(V)
        G = [[(e[0], 0, e[1]) for e in links] for links in self.E]
        
        parents = [-1 for v in self.V]

        while self.bst(G, parents):

            # reconstruct reverse path
            s = 0
            it = len(G) - 1
            revpath = [it]
            add = float('inf')
            while it != s:
                old = it
                it = parents[it]
                revpath.append(it)
                add = min(add, G[it][old]) # TODO, find old from G

            total += add

            # reverse
            for i in range(len(G)-1, -1, -1):
                G[i]. 
        


