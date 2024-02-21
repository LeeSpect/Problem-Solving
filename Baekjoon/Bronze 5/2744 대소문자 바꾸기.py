import sys; input=sys.stdin.readline

up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
down='abcdefghijklmnopqustuvwxyz'

k=input().rstrip()
ans=''
for i in range(len(k)):
    if k[i] in up:
        ans+=k[i].lower()
    else:
        ans+=k[i].upper()
print(ans)
