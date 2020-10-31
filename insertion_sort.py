#!/usr/bin/python

def insertion_sort(A):
    n = len(A)
    for j in range(1,n):
        # take j-th value
        key = A[j]
        i = j - 1

        # swap until previous values are major then the current (j-th)
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        
        # assign the next one
        A[i+1] = key
    return A

A = [3, 2, 1, 0]
print(insertion_sort(A))
