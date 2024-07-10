import sys
input = sys.stdin.readlines

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    
    graph = [[] for _ in range(m+1)]
    for _ in range(n):
        x, y ,z = map(int, input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
        