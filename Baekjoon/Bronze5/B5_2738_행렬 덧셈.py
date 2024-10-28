import sys; input=sys.stdin.readline

n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    k=list(map(int,input().split()))
    for j in range(m):
        l[i][j]+=k[j]
for i in range(n):
    print(*l[i])
