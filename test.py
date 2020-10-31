#!/usr/bin/python

import heap
import sys

from priorqueue import Priority_queue

def printlevel(n):
    print("Index: ", n)
    print("Level: ", heap.levelof(n))
    print("Position: ", heap.posof(n))
    print()

"""
for n in range(16):
    print("Central")
    printlevel(n)

    print("Left")
    printlevel(heap.left(n))

    print("Right")
    printlevel(heap.right(n))

    print()
"""

#### HEAP test

print("\nTesting Heap\n")

#L = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
L = [5, 14, 10, 8, 7, 9, 3, 2, 4, 1]

print("Initial L = ", L)

H = heap.Heap(L)

print("Heaped L = ", H)

H.build_heap()

print("Heaped L (should be equal)= ", H)

L = heap.heapsort(L)

print("Sorted L = ", L)

#### Priority queue test

print("\nTesting Priority queue\n")

S = Priority_queue([9, 8, 5, 6, 7, 1, 0, 4, 1, 3])
print("Original S: ", S)

M = S.extract_max()
print("Maximum extracted: ", M)
print("S after maximum extracted: ", S, "\n")

S = Priority_queue([12, 8, 5, 6, 7, 1, 0, 4, 1, 3])
print("New original S: ", S)
print("Heap increase key: ", S.increase_key(7, 10), "\n")

S = Priority_queue([12, 8, 5, 6, 7, 1, 0, 4, 1, 3])
print("New original S: ", S)
print("Heap insert key: ", S.insert(10), "\n")


