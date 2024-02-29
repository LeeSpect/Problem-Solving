import sys

l = list(map(int, sys.stdin.readline().split()))
x,y,r = map(int, sys.stdin.readline().split())
if x in l:
    print(l.index(x)+1)
else:
    print(0)
