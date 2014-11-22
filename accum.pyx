# accum.pyx
def main():
    cdef int i, n, accum
    accum = 0
    n = 10**7
    for i in range(n):
        accum += i
    print i

main()