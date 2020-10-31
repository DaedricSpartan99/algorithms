#!/usr/bin/python

# L1 and L2 are ordered lists
# complex: theta(len(L1) + len(L2))
def merge(L1, L2):
    L1.append(float('inf'))
    L2.append(float('inf'))
    out = []
    while len(L1) > 1 or len(L2) > 1:
        if L1[0] < L2[0]:
            out.append(L1[0])
            del L1[0]
        else:
            out.append(L2[0])
            del L2[0]
    return out

# merge sort algorithm
# complex: theta(N log(N)), N = len(L)
def m_sort(L):
    N = len(L)
    if N == 2:
        if L[1] < L[0]:
            L[0], L[1] = L[1], L[0] # swap couple
    elif N > 2:
        split = N // 2
        L1 = m_sort(L[0:split])
        L2 = m_sort(L[split:])
        L = merge(L1,L2)
    return L
