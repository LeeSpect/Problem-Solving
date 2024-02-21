import sys; input=sys.stdin.readline
import heapq

def dijkstra(N,G,X):
    dist=[float('inf') for i in range(N+1)]; dist[0]=0
    dist[X]=0
    heap=[(0,X)]

    while heap:
        wei,now=heapq.heappop(heap)
        if dist[now]<wei:
            continue

        for i in G[now]:
            next_wei=wei+i[1]
            if dist[i[0]]>next_wei:
                dist[i[0]]=next_wei
                heapq.heappush(heap,(next_wei,i[0]))
    return dist

def main():
    N,M,X=map(int,input().split())
    G=[[] for i in range(N+1)]
    G2=[[] for i in range(N+1)]
    for _ in range(M):
        start,end,T=map(int,input().split())
        G[start].append((end,T))
        G2[end].append((start,T))
    l=dijkstra(N,G,X)
    l2=dijkstra(N,G2,X)
    for i in range(1,N+1):
        l[i]+=l2[i]
    print(max(l))

if __name__=='__main__':
    main()
