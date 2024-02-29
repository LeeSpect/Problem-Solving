import sys; input=sys.stdin.readline
from itertools import product

n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
ansl=list(set(product(l,repeat=m)))
ansl.sort()
t=len(ansl)
for i in range(t):
    print(*ansl[i])
