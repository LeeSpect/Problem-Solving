import sys

input = sys.stdin.readline

comb = [[0 for _ in range(53)] for _ in range(53)]

for i in range(53):
    comb[i][0] = 1

for i in range(1, 53):
    for j in range(1, 53):
        comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % 10007


N = int(input())
ans = 0

for i in range(1, 14):
    if N-4*i < 0:
        break
    if i%2 == 1:
        ans = (ans + comb[52-4*i][N-4*i]*comb[13][i]) % 10007
    else:
        ans = (ans - (comb[52-4*i][N-4*i]*comb[13][i]) % 10007 + 10007) % 10007

print(ans)