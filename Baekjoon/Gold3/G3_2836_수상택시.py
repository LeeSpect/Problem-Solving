import sys
import heapq as hq

input = sys.stdin.readline

N, M = map(int, input().split())

# 보트 이동 규칙: in 인덱스 첫번째부터 +
# D1, D2, visited = [False]

visited = [False] * 300001
points = sorted([tuple(map(int, input.rstrip())) for _ in range(N)])
boat = [(M, 0, 0)]

now, ans = 0, 0
for i in range(1, len(points)+1):
    point = points[i-1]
    start, end = point
    

print(ans)