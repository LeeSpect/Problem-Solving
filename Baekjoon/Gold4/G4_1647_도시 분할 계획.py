# Union을 사용하여 최소 스패닝 트리를 만든 다음, 스패닝 트리를 구성하는 간선 중 가장 비싼 간선을 뺀다

import sys
import heapq
input = sys.stdin.readline

def find_parents(parents, node):
    while parents[node] != node:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return parents[node]

def Union(parents, node1, node2):
    a = find_parents(parents, node1)
    b = find_parents(parents, node2)
    if a == b:
        return False
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return True

def main():
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    edges = []
    for i in range(M):
        A, B, C = map(int, input().split())
        heapq.heappush(edges, (C,A,B))
    weigh = 0
    max_cost = 0
    while edges:
        cost, node1, node2 = heapq.heappop(edges)
        if Union(parents, node1, node2):
            weigh += cost
            max_cost = max(max_cost, cost)
    print(weigh - max_cost)

if __name__ == '__main__':
    main()
