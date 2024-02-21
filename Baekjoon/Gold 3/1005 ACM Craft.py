# 리스트의 인덱스는 각 건물을 의미하고, 리스트의 인덱스 값은 해당 건물을 건설한 후 이어서 건설할 수 있는 건물의 번호이다.
# 리스트의 인덱스 값을 건설 시간을 기준으로 정렬한다.

# ----------------------------------------------------------------------------------------------------
# 틀린 코드: for 문을 돌며, before_con이 비어있는 건물을 하나씩 sol 함수에 넣고 최소값을 찾아가는 방식이었습니다.
# 하지만 before_con이 비어있는 건물이라면 모두 동시에 건설이 시작될 수 있음을 간과했습니다.
import sys; input=sys.stdin.readline
import heapq

def sol(Ds, W, start_X, next_cons=[], before_cons=[]):
    next_conss, before_conss = [i[:] for i in next_cons], [i[:] for i in before_cons]
    if not before_conss[start_X] and start_X == W:
        return Ds[start_X-1]
    heap = [(Ds[start_X-1], start_X)]
    while heap:
        wei, now_con = heapq.heappop(heap)
        while next_conss[now_con]:
            next_con = next_conss[now_con].pop()
            if before_conss[next_con]:
                before_conss[next_con].remove(now_con)
            else:
                heapq.heappush(heap, (wei+Ds[next_con-1], next_con))
            if not before_conss[next_con]:
                if next_con == W:
                    return wei+Ds[next_con-1]
                else:
                    heapq.heappush(heap, (wei+Ds[next_con-1], next_con))
    return float('inf')

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        Ds = list(map(int, input().split()))
        next_cons = [[] for i in range(N+1)]
        before_cons = [[] for i in range(N+1)]
        start_X = 0
        for i in range(K):
            X, Y = map(int, input().split())
            next_cons[X].append(Y)
            before_cons[Y].append(X)
            if i == 0:
                start_X = X
        W = int(input())
        mini = float('inf')
        for i in range(1, N+1):
            if not before_cons[i]:
                mini = min(mini, sol(Ds, W, i, next_cons, before_cons))
        print(mini)

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: before_con이 빈 건물들을 동시에 건설할 수 있도록 a_before_con이라는 리스트를 새로 선언하여 append 해준 후,
# sol 함수 구동 초반에, 해당하는 건물을 모두 heap에 넣어 구현하였습니다.
import sys; input=sys.stdin.readline
import heapq

def sol(Ds, W, next_cons, before_cons, a_before_cons):
    heap = []
    mini=float('inf')
    for start_X in a_before_cons:
        if not before_cons[start_X] and start_X == W:
            return Ds[start_X-1]
        heapq.heappush(heap, (Ds[start_X-1], start_X))
    while heap:
        wei, now_con = heapq.heappop(heap)
        while next_cons[now_con]:
            next_con = next_cons[now_con].pop()
            if before_cons[next_con]:
                before_cons[next_con].remove(now_con)
            else:
                heapq.heappush(heap, (wei+Ds[next_con-1], next_con))
            if not before_cons[next_con]:
                if next_con == W:
                    return wei+Ds[next_con-1]
                else:
                    heapq.heappush(heap, (wei+Ds[next_con-1], next_con))

def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        Ds = list(map(int, input().split()))
        next_cons = [[] for i in range(N+1)]
        before_cons = [[] for i in range(N+1)]
        start_X = 0
        for i in range(K):
            X, Y = map(int, input().split())
            next_cons[X].append(Y)
            before_cons[Y].append(X)
            if i == 0:
                start_X = X
        W = int(input())
        mini = float('inf')
        a_before_cons=[]
        for i in range(1, N+1):
            if not before_cons[i]:
                a_before_cons.append(i)
        print(sol(Ds, W, next_cons, before_cons, a_before_cons))

if __name__=='__main__':
    main()
