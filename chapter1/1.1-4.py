""" Consider the problem of adding two n-bit binary integers
    stored in two n-element arrays A and B.  The sum of the 
    two integers should be stored in binary form in an 
    (n + 1)-element array C.  Write code for adding the two
    integers
"""

def main():
    n = 4
    A = [0, 1, 1, 1]
    B = [1, 0, 1, 1]
    C = [0, 0, 0, 0, 0]

    C = add_binary_arrays(A, B, n)
    print C
    return

def add_binary_arrays(A, B, n):
    C = [0 for i in range(n + 1)]
    carry = 0
    for i in range(n):
        a = A[i]
        b = B[i]
        if a == 1 and b == 1:
            if carry == 0:
                c = 0
                carry = 1
            else:
                c = 1
                carry = 1
        else:
            if carry == 1 and (a == 1 or b == 1):
                c = 0
                carry = 1
            else:
                c = a + b
                carry = 0

        C[i] = c

    if carry == 1:
        C[-1] = carry

    return C

if __name__ == "__main__":
    main()
