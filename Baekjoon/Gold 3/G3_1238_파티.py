import sys
import heapq as hq

input = sys.stdin.readline

def dij(N, graph, X):
    dist = [float('inf') for _ in range(N+1)]
    dist[X] = 0
    heap = [(0, X)]
    
    while heap:
        wei, now = hq.heappop(heap)
        if dist[now] < wei:
            continue
        
        for next in graph[now]:
            next_wei = wei + next[1]
            if dist[next[0]] > next_wei:
                dist[next[0]] = next_wei
                hq.heappush(heap, (next_wei, next[0]))
    return dist                

def main():
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)] # reverse graph
    
    for _ in range(M):
        start, end, T = map(int, input().split())
        graph[start].append((end, T))
        graph2[end].append((start, T))
    
    l = dij(N, graph, X)
    l2 = dij(N, graph2, X)
    
    ans_list = [l[i] + l2[i] for i in range(1, N+1)]
    print(max(ans_list))

if __name__ == "__main__":
    main()