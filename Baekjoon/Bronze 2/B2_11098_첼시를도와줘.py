# 110272 KB / 132 ms
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = int(input())
    l = []
    for k in range(t):
        data = input().split()
        l.append((-int(data[0]), data[1]))
    l.sort()
    print(l[0][1])
