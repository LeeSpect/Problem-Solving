import sys
input=sys.stdin.readline
s=[0.148392,0.24948,0.06237]
l=list(map(int,input().split()))
ans=0
for i in range(3):
    ans+=l[i]*s[i]
print(ans)
