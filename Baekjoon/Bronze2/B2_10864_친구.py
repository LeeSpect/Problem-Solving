# 109108 KB / 116 ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    l[a] += 1
    l[b] += 1

print(*l[1:], sep='\n')