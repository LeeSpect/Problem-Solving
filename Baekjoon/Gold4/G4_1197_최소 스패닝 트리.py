# 126,892 KB / 732 ms
import sys
import heapq

input = sys.stdin.readline

def find_parent(parents, node):
    while parents[node] != node:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return parents[node]

def Union(parents, node1, node2):
    a = find_parent(parents, node1)
    b = find_parent(parents, node2)
    if a == b:
        return False
    elif a < b:
        parents[b] = a
    else:
        parents[a] = b
    return True

def main():
    V, E = map(int, input().split())
    parents = [i for i in range(V+1)]
    edges = []
    for i in range(E):
        A, B, C = map(int, input().split())
        heapq.heappush(edges, (C, A, B))
    weigh = 0
    while edges:
        cost, node1, node2 = heapq.heappop(edges)
        if Union(parents, node1, node2):
            weigh += cost
    print(weigh)

if __name__ == '__main__':
    main()