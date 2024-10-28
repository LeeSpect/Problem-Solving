L = [1, 1, 2, 2, 2, 8]
F = list(map(int, input().split()))

for i in range(len(L)):
    print(L[i]-F[i], end=' ')
