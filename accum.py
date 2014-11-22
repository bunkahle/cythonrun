import time

#  accum.py
def main():
    # def int i, n, accum
    accum = 0
    n = 10**7
    for i in range(n):
        accum += i
    print i

start_time = time.clock()
main()
print time.clock() - start_time, "seconds execution time."
