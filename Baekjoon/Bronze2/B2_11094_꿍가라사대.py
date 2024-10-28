# 109240 KB / 120 ms
import sys
input=sys.stdin.readline

N = int(input())
for _ in range(N):
    l = list(map(str, input().split()))
    if l[0] == 'Simon' and l[1] == 'says':
        print(" " + ' '.join(l[2:]))