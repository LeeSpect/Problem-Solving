import sys

def fac(n):
    if n == 0: return 1
    elif n == 1: return 1
    else:
        return n * fac(n-1)

n = int(sys.stdin.readline())
print(fac(n))
