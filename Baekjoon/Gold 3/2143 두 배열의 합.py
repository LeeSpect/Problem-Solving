# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 중간중간 탈출할 수 있도록 구현하였지만 시간초과 발생
import sys; input=sys.stdin.readline

def main():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    ap1, ap2, bp1, bp2 = 0, 0, 0, 0
    sum_A, sum_B = A[0], B[0]
    cnt = 0
    for a1 in range(n):
        sum_A = A[a1]
        if sum_A >= T:
            continue
        for a2 in range(a1,n):
            if a1 != a2:
                sum_A += A[a2]
            if sum_A >= T:
                continue
            for b1 in range(m):
                sum_B = B[b1]
                if sum_A + sum_B >= T:
                    if sum_A + sum_B == T:
                        cnt += 1
                    continue
                for b2 in range(b1,m):
                    if b1 != b2:
                        sum_B += B[b2]
                    if sum_A + sum_B == T:
                        cnt += 1
    print(cnt)

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 시간 초과
# A 배열과 B 배열 중 작은 크기의 배열을 골라서(메모리 절약) 부분합의 모든 경우의 수를 저장한다.
# 저장한 리스트를 정렬하면 시간에서 효율적이다.
# 그리고 남은 배열를 돌면서 저장된 결과와 조합해본다.
import sys; input=sys.stdin.readline

def make_partsum(t, L):
    partsum = []
    s = 0
    for i in range(t):
        s = L[i]
        for j in range(i, t):
            if i != j:
                s += L[j]
            partsum.append(s)
    partsum.sort()
    return partsum

def count(t, L, partsum, T):
    total = 0
    cnt = 0
    for i in range(t):
        total = L[i]
        for j in range(i, t):
            if i != j:
                total += L[j]
            for part in partsum:
                if total + part == T:
                    cnt += 1
                elif total + part > T:
                    break
    return cnt

def main():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    if n < m:
        partsum = make_partsum(n, A)
        print(count(m, B, partsum, T))
    else:
        partsum = make_partsum(m, B)
        print(count(n, A, partsum, T))

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: partsum 리스트를 사전형으로 수정하여 시간을 단축했다.
import sys; input=sys.stdin.readline

def make_partsum(t, L):
    partsum = {}
    s = 0
    for i in range(t):
        s = L[i]
        for j in range(i, t):
            if i != j:
                s += L[j]
            if partsum.get(s):
                partsum[s] += 1
            else:
                partsum[s] = 1
    return partsum

def count(t, L, partsum, T):
    total = 0
    cnt = 0
    for i in range(t):
        total = L[i]
        for j in range(i, t):
            if i != j:
                total += L[j]
            if T - total in partsum:
                cnt += partsum[T-total]
    return cnt

def main():
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    if n < m:
        partsum = make_partsum(n, A)
        print(count(m, B, partsum, T))
    else:
        partsum = make_partsum(m, B)
        print(count(n, A, partsum, T))

if __name__=='__main__':
    main()
