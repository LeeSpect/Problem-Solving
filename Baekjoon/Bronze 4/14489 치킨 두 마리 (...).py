import sys

a,b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
if a+b < 2*c:
    print(a+b)
else:
    print(a+b-c*2)
