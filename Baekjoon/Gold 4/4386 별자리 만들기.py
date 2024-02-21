# 두 별 사이를 선으로 긋고, 그 선들의 최소 비용을 구하는 문제이므로 최소 스패닝 트리를 이용한다.

import sys; input=sys.stdin.readline
import heapq

def find_parent(parents,node):
    if parents[node]!=node:
        parents[node]=find_parent(parents,parents[node])
    return parents[node]

def make_star(parents,node1,node2):
    a=find_parent(parents,node1)
    b=find_parent(parents,node2)
    if a==b:
        return 0
    if a>b:
        parents[a]=b
    else:
        parents[b]=a
    return 1

def main():
    n=int(input())
    G=[]
    heap=[]
    for i in range(n):
        x,y=map(float,input().split())
        for g in G:
            wei=(abs(g[0]-x)**2+abs(g[1]-y)**2)**0.5
            heapq.heappush(heap,(wei,i,g[2]))
        G.append((x,y,i))
    parents=[i for i in range(n+1)]
    ans=0
    while heap:
        wei,node1,node2=heapq.heappop(heap)
        if make_star(parents,node1,node2):
            ans+=wei
    print(f'{ans:0.2f}')

if __name__=='__main__':
    main()
