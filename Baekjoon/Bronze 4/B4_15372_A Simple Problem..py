import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    if n**0.5%1 == 0:
        print(int(n**0.5))
    else: print(n)
