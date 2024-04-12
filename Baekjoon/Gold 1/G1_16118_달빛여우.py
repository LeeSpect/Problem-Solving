import sys
import heapq as hq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d*2))
    graph[b].append((a, d*2))

dist_fox = [float('inf') for _ in range(N+1)]
dist_fox[1] = 0
heap = [(0, 1)]
while heap:
    wei, now = hq.heappop(heap)
    if wei > dist_fox[now]: continue

    for next_node, dist in graph[now]:
        next_wei = dist_fox[now] + dist
        if next_wei < dist_fox[next_node]:
            dist_fox[next_node] = next_wei
            hq.heappush(heap, (next_wei, next_node))

dist_wolf = [[float('inf')]*2 for _ in range(N+1)]
dist_wolf[1][0] = 0
heap = [(0, 1, 0)]
while heap:
    wei, now, end = hq.heappop(heap)
    if wei > dist_wolf[now][end]: continue
    next_end = (end+1)%2

    for next_node, dist in graph[now]:
        next_wei = wei + dist*2 if next_end==0 else wei+dist//2
        if dist_wolf[next_node][next_end] > next_wei:
            dist_wolf[next_node][next_end] = next_wei
            hq.heappush(heap, (next_wei, next_node, next_end))

print(sum([int(dist_fox[i]<min(dist_wolf[i][0],dist_wolf[i][1])) for i in range(2,N+1)]))