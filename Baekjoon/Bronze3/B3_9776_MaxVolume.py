import sys; input = sys. stdin.readline

PIE = 3.14159

n = int(input())
ans = -1
for _ in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == 'C':
        ans = max(ans, (1/3) * PIE * float(arr[1])**2 * float(arr[2]))
    elif arr[0] == 'L':
        ans = max(ans, PIE * float(arr[1])**2 * float(arr[2]))
    else:
        ans = max(ans, (4/3) * PIE * float(arr[1])**3)
print(f'{ans:.3f}')
