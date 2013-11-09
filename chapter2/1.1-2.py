#! /usr/bin/env python
"""
    Rewrite the insertion-sort procedure to sort into nonincreasing
    insead of nondecreasing order.
"""
def dec_insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

def main():
    l = [5, 2, 0, 3, 8, 7]

    print l

    l = dec_insertion_sort(l)

    print l


if __name__ == "__main__":
    main()
