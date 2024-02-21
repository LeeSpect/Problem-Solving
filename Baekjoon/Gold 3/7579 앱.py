# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 이 코드처럼 cost가 작은 것부터 계산하면 최적해를 구할 수 없습니다.
# 제거해야 하는 메모리가 2000인데 cost가 1이고 차지하는 메모리의 크기가 1인 앱이 20개,
# cost가 2이고 차지하는 메모리의 크기가 2000인 앱이 1개 있다면, 최적의 비용인 2를 출력하지 않는다.
import sys; input=sys.stdin.readline
import heapq

def main():
    N, M = map(int, input().split())
    Actives = list(map(int, input().split()))
    Costs = list(map(int, input().split()))
    heap = []
    for i in range(N):
        heapq.heappush(heap, (Costs[i], -Actives[i]))
    cost = 0
    while M:
        c, m = heapq.heappop(heap)
        M += m
        cost += c
    print(cost)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------
# 틀린 수정 코드1: 배낭 문제 알고리즘을 dp로 구현하였습니다. dp의 크기가 너무 커서 메모리 초과가 발생했습니다.
import sys; input=sys.stdin.readline

def Knapsack(N, M, Memories, Costs):
    dp = [[float('inf') for _ in range(M+1)] for i in range(N+1)]
    for item in range(1, N+1):
        for capa in range(1, M+1):
            if capa - Memories[item] <= 0:
                dp[item][capa] = min(dp[item-1][capa], Costs[item])
            else:
                dp[item][capa] = min(dp[item-1][capa], dp[item-1][capa-Memories[item]] + Costs[item])
    return dp[-1][-1]

def main():
    N, M = map(int, input().split())
    Memories = [float('inf')] + list(map(int, input().split()))
    Costs = [float('inf')] + list(map(int, input().split()))
    print(Knapsack(N, M, Memories, Costs))

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------
# 틀린 수정 코드2: dp의 column을 Memories의 총합으로 대체하였지만 여전히 메모리 초과가 발생했습니다.
import sys; input=sys.stdin.readline

def Knapsack(N, M, Memories, Costs, total):
    dp = [[float('inf') for _ in range(total+1)] for i in range(N+1)]
    for item in range(1, N+1):
        for capa in range(1, total+1):
            if capa - Memories[item] <= 0:
                dp[item][capa] = min(dp[item-1][capa], Costs[item])
            else:
                dp[item][capa] = min(dp[item-1][capa], dp[item-1][capa-Memories[item]] + Costs[item])
    return dp[-1][M]

def main():
    N, M = map(int, input().split())
    Memories = [0] + list(map(int, input().split()))
    Costs = [float('inf')] + list(map(int, input().split()))
    total = sum(Memories)
    Memories[0] = float('inf')
    print(Knapsack(N, M, Memories, Costs, total))

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: dp의 column을 Costs의 총합으로 두고 구현하여 메모리 초과를 해결하였습니다.
import sys; input=sys.stdin.readline

def Knapsack(N, M, Memories, Costs):
    total_costs = sum(Costs)
    dp = [[0 for _ in range(total_costs+1)] for i in range(N+1)]
    min_cost = float('inf')
    for memory in range(1, N+1):
        for cost in range(1, total_costs+1):
            if Costs[memory] <= cost:
                dp[memory][cost] = max(dp[memory-1][cost-Costs[memory]]+Memories[memory], dp[memory-1][cost])
            else:
                dp[memory][cost] = max(dp[memory][cost-1], dp[memory-1][cost])
            if min_cost > cost and dp[memory][cost] >= M:
                min_cost = cost
    return min_cost

def main():
    N, M = map(int, input().split())
    Memories = [0] + list(map(int, input().split()))
    Costs = [0] + list(map(int, input().split()))
    print(Knapsack(N, M, Memories, Costs))

if __name__ == "__main__":
    main()
