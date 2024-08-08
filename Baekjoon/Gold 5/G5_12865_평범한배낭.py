# 215,196 KB / 500 ms
import sys
import heapq

input = sys.stdin.readline

def knapsack_DP(l, n, k):
    D = [[0] * (k + 1)]
    
    for i in range(1, n+1):
        D.append([])    
        for capa in range(k + 1):
            if v == 0:
                D[i].append(0)
            elif l[i-1][0] > capa:
                D[i].append(D[i-1][capa])
            else:
                D[i].append(max(D[i-1][capa], D[i-1][capa-l[i-1][0]] + l[i-1][1]))
    return D[-1][-1]

n, k = map(int, input().split())
l = []
for i in range(n):
    w, v = map(int, input().split())
    heapq.heappush(l, (w, v))
print(knapsack_DP(l, n, k))