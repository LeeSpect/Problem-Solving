# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 무지성으로 해보다가 틀렸습니다.
# 질문 게시판에서 위상정렬을 사용하라는 힌트를 얻었으니 위상정렬 공부를 해야겠습니다.
import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def line_up(visited, down, up, k, ansl):
    while up[k]:
        q = up[k].pop()
        if q not in visited:
            visited.add(q)
            line_up(visited, down, up, q, ansl)
    ansl.append(k)
    while down[k]:
        q = down[k].pop()
        if q not in visited:
            visited.add(q)
            line_up(visited, down, up, q, ansl)

def main():
    N, M = map(int, input().split())
    up = [[] for _ in range(N+1)]
    down = [[] for _ in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())
        down[A].append(B)
        up[B].append(A)
    visited = set()
    ansl = []
    for i in range(1, N+1):
        if i not in visited:
            visited.add(i)
            line_up(visited, down, up, i, ansl)
    print(*ansl)

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 위상정렬을 이용하여 구현하였습니다.
import sys; input=sys.stdin.readline

def line_up(in_degree, down, up, ansl):
    while in_degree:
        i = in_degree.pop()
        ansl.append(i)
        while down[i]:
            q = down[i].pop()
            up[q] -= 1
            if not up[q]:
                in_degree.append(q)

def main():
    N, M = map(int, input().split())
    up = [0 for _ in range(N+1)]
    down = [[] for _ in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())
        down[A].append(B)
        up[B] += 1
    in_degree = []
    for i in range(1, N+1):
        if not up[i]:
            in_degree.append(i)
    ansl = []
    line_up(in_degree, down, up, ansl)
    print(*ansl)

if __name__=='__main__':
    main()
