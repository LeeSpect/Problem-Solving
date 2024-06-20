import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
start, end = 1, K

# K번째로 큰 값 = K보다 작거나 같은 수의 개수가 K개인 값
# 1~K까지의 수 중에서 K보다 작거나 같은 수의 개수를 찾는 문제

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    
    # N*N에서 20보다 작거나 같은 수는
    # 1행  1 ~ 20          -> 20//1 개
    # 2행  2,4,6,8...      -> 20//2 개
    # 3행  3,6,9,12...     -> 20//3 개
    # 4행  4,8,12,16,20... -> 20//4 개
    # ...
    # N행  N,N*2,N*3...    -> 20//N 개
    # ?//i가 N보다 큰 경우가 존재하므로 최대 N까지만 갖게 설정

    for i in range(1, N+1):    # 1~N까지의 행을 기준으로
        cnt += min(mid//i, N)  # mid//i가 N보다 큰 경우가 존재하므로 최대 N까지만 갖게 설정
    if cnt >= K:               # 찾는 값보다 크거나 같은 경우
        result = mid            # 결과값 저장
        end = mid - 1           # 범위를 줄여줌
    else:
        start = mid + 1         # 범위를 늘려줌
print(result)