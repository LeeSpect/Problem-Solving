import sys; input=sys.stdin.readline

t=int(input())
for i in range(t):
    k=input().rstrip()
    print(k[0]+k[-1])
