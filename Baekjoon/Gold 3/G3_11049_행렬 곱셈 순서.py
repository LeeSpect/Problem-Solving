# ----------------------------------------------------------------------------------------------------
# 틀린 코드: DP로 풀지 않았을 때의 코드
# 반례 :
# 5
# 1 2
# 2 3
# 3 5
# 5 6
# 6 100
import sys; input=sys.stdin.readline
import heapq

def main():
    N = int(input())
    Q = []
    heap = []
    for i in range(N):
        r, c = map(int, input().split())
        Q.append((r,c))
        if i != N-1:
            heapq.heappush(heap, (-c, c))
    total = 0
    while heap:
        print(total, Q)
        k = heapq.heappop(heap)
        i = 0
        temp = (float('inf'), 0)
        for q in Q:
            if i == N-1:
                break
            if q[1] == k[1]:
                temp = min(((q[0] * q[1] * Q[i+1][1]), i), temp)
            i += 1
        total += temp[0]
        Q[temp[1]] = (Q[temp[1]][0], Q[temp[1]+1][1])
        Q.pop(temp[1]+1)
        N -= 1

    print(total)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 수정 코드: 정말 어려운 문제였습니다.
# 참조 블로그를 보고 나서야 DP 인덱스를 뭐로 설정해야 하는지 알 수 있었고,
# 그리고 나서도 점화식을 적용하는데 어려움이 있었다.
# 3중 반복문 안에서 i, j, k를 적절히 조정하여 DP[i][j]의 값을 설정하는 과정이 어려웠습니다.

# 참조: https://velog.io/@turtle601/%EB%B0%B1%EC%A4%80-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-11049%EB%B2%88
import sys; input=sys.stdin.readline

def main():
    N = int(input())
    Q = []
    for _ in range(N):
        a, b = map(int, input().split())
        Q.append((a, b))
    dp = [[float('inf')] * (N) for i in range(N)]
    for j in range(N):
        for i in range(j, -1, -1):
            if i == j:
                dp[i][j] = 0
            else:
                for k in range(j-i):
                    dp[i][j] = min(dp[i][j], dp[i][j-k-1] + dp[j-k][j] + Q[i][0]*Q[j-k][0]*Q[j][1])
    print(dp[0][-1])

if __name__ == "__main__":
    main()
