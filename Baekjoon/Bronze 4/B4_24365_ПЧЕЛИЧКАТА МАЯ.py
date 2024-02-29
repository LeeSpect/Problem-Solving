import sys
from collections import deque
input=sys.stdin.readline

d=[[0],[1],[2]]
l=list(map(int,input().split()))
for i in range(3):
    d[i].append(l[i])
ans=sum(l)//3
d.sort(key=lambda x: x[1])
print(abs(d[2][0]-d[0][0])*(ans-d[0][1])+abs(d[2][0]-d[1][0])*(ans-d[1][1]))
