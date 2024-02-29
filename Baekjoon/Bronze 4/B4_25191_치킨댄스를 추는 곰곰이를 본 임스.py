import sys; input=sys.stdin.readline

c=int(input())
a,b=map(int,input().split())
a//=2
print(a+b if a+b<c else c)
