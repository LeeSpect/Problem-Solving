import sys
input = sys.stdin.readline

def find_parent(node):
    while node != parents[node]:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return parents[node]

def union(node1, node2):
    a = find_parent(node1)
    b = find_parent(node2)
    
    if a == b:
        return False
    elif a < b:
        parents[b] = a
    else:
        parents[a] = b
    return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    parents = [i for i in range(m+1)]
    cost = 0
    
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])
    
    for edge in edges:
        u, v, w = edge
        if find_parent(u) != find_parent(v):
            union(u, v)
        else:
            cost += w
    print(cost)