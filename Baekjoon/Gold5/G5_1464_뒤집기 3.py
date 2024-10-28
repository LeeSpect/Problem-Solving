import sys
from collections import deque
input=sys.stdin.readline

s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

l=deque(list(input().rstrip()))
n=len(l)
D=deque()
for i in range(n):
    k=l.popleft()
    if not D:
        D.append(k)
    elif s.index(k)<=s.index(D[0]):
        D.appendleft(k)
    else:
        D.append(k)
print(''.join(list(D)))
