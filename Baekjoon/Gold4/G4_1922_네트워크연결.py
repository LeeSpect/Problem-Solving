import sys
input = sys.stdin.readline

def find_parent(parents, node1):
    while parents[node1] != node1:
        parents[node1] = parents[parents[node1]]
        node1 = parents[node1]
    return parents[node1]

def union(parents, node1, node2):
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
    N = int(input().strip())
    M = int(input().strip())
    edges = []

    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        edges.append((c, a-1, b-1))  # 노드 번호를 0부터 시작하도록 조정

    edges.sort()  # 비용 기준으로 간선을 정렬

    parents = [i for i in range(N)]
    mst_cost = 0
    mst_edges = 0

    for cost, u, v in edges:
        if union(parents, u, v):
            mst_cost += cost
            mst_edges += 1
            if mst_edges == N - 1:
                break

    print(mst_cost)

if __name__ == "__main__":
    main()
