# /usr/bin/env python

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]

        i = j - 1

        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

    return A

def main():
    l = [5, 2, 4, 6, 1, 3]

    print l

    l = insertion_sort(l)

    print l

    return


if __name__ == "__main__":
    main()
