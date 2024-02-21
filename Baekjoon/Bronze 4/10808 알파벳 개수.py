import sys; input=sys.stdin.readline

ans='abcdefghijklmnopqrstuvwxyz'
l=[]
k=input().rstrip()
for i in range(26):
    l.append(k.count(ans[i]))
print(*l)
