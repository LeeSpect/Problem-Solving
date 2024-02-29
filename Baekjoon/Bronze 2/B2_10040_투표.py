import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
score = [0 for _ in range(N)]
B = [int(input()) for _ in range(M)]

for m in range(M):
    for n in range(N):
        if A[n] <= B[m]:
            score[n] += 1
            break

print(score.index(max(score))+1)