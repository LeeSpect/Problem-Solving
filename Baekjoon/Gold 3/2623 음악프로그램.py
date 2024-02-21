# 위상정렬 문제입니다. Union-Find이라고 착각하지 맙시다.
import sys; input=sys.stdin.readline

def topological_sort(in_degree, down, up):
    ansl = []
    while in_degree:
        i = in_degree.pop()
        ansl.append(i)
        while down[i]:
            q = down[i].pop()
            up[q] -= 1
            if not up[q]:
                in_degree.append(q)
    return ansl

def main():
    N, M = map(int, input().split())
    up = [0 for _ in range(N+1)]
    down = [[] for _ in range(N+1)]
    for i in range(M):
        l = list(map(int, input().split()))
        for j in range(1, l[0]):
            up[l[j+1]] += 1
            down[l[j]].append(l[j+1])
    in_degree = []
    for i in range(1, N+1):
        if not up[i]:
            in_degree.append(i)
    ansl = topological_sort(in_degree, down, up)
    if len(ansl) != N:
        print(0)
    else:
        for i in range(N):
            print(ansl[i])

if __name__ == "__main__":
    main()
