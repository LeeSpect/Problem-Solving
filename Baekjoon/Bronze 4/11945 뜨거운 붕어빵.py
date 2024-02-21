import sys; input=sys.stdin.readline

n,m=map(int,input().split())
for i in range(n):
    k=input().rstrip()
    print(k[::-1])
