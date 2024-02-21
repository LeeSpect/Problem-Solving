import sys; input=sys.stdin.readline
import heapq

def sol(n,G,start,end):
    dist=[[float('inf'),[]] for _ in range(n+1)]
    dist[start][0]=0
    dist[start][1].append(start)
    heap=[(dist[start][0], start)]
    
    while heap:
        wei,now=heapq.heappop(heap)
        if dist[now][0]<wei:
            continue
        for i in G[now]:
            next_wei=wei+i[1]
            if dist[i[0]][0]>next_wei:
                dist[i[0]][0]=next_wei
                dist[i[0]][1]=dist[now][1][:]+[i[0]]
                heapq.heappush(heap,(dist[i[0]][0],i[0]))
    print(dist[end][0])
    print(len(dist[end][1]))
    print(*dist[end][1])

def main():
    n=int(input())
    m=int(input())
    G=[[] for _ in range(n+1)]
    for _ in range(m):
        s,e,c=map(int,input().split())
        G[s].append((e,c))
    start,end=map(int,input().split())
    sol(n,G,start,end)
    
if __name__=='__main__':
    main()
