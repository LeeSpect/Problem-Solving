import sys
input=sys.stdin.readline

t,m,tt,mm=map(int,input().split())
m+=t*60
mm+=tt*60
if m>mm:
    mm+=24*60
ans=mm-m
print(ans, ans//30)
