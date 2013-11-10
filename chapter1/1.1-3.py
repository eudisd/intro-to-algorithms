#! /usr/bin/env python


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
