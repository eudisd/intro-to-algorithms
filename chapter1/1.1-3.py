#! /usr/bin/env python

"""
    Write code for linear search, which scans through the sequence
    looking for v.
    Input: A sequence of n numbers A = <a1, a2,...,an> and a value v.
    Output: An index i such that v = A[i] or the special value NIL if v
    does not appear in A.
"""

def linear_search(A, v):
    for i in range (len(A)):
        if A[i] == v:
            return i

    return None

def main():
    l = [2, 3, 5, 0, 8]
    print linear_search(l, 5)
    return


if __name__ == "__main__":
    main()
