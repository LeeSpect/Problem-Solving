import sys
input = sys.stdin.readline

maxi, r, c = 0, 0, 0
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] > maxi:
            maxi = arr[j]
            r, c = i, j
print(maxi)
print(r + 1, c + 1)
