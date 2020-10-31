#!/usr/bin/python

class fms_t:
    def __init__(self, low, high, sumover):
        self.low = low
        self.high = high
        self.sumover = sumover

    def __ge__(self, other):
        return self.sumover >= other.sumover


def find_max_subarray(A, low, high):
    if low == high:
        return fms_t(low, high, 0) # no elements
    elif (low + 1) == high:
        return fms_t(low, high, A[low]) # trivial case
    
    # split A into A[low, mid[ and A[mid, high[
    mid = (low + high) // 2

    # compute divisions
    left = find_max_subarray(A, low, mid)
    right = find_max_subarray(A, mid, high)
    cross = find_max_crossing(A, low, mid, high)

    # compare results
    if left >= right and left >= cross:
        return left
    elif right >= left and right >= cross:
        return right
    else:
        return cross


def find_max_crossing(A, low, mid, high):
    # find a maximum subarray of the form A[i, mid[
    s = 0
    left_sum = float('-inf')
    max_left = mid-1
    for i in range(mid-1, low-1, -1):
        s += A[i]
        if s > left_sum:
            left_sum = s
            max_left = i

    # find a maximum subarray of the form A[mid, high[
    s = 0
    right_sum = float('-inf')
    max_right = mid
    for j in range(mid, high):
        s += A[j]
        if s > right_sum:
            right_sum = s
            max_right = j

    # merge them together
    return fms_t(max_left, max_right, left_sum + right_sum)



