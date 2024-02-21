import sys

a,b,c = map(int, sys.stdin.readline().split())

if a<=c and c<=b-1:
    print(1)
else:
    print(0)
