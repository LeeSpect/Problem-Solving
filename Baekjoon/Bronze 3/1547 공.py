n = int(input())
ans = 1
for i in range(n):
    a,b = map(int, input().split())
    if a == ans:
        ans = b
    elif b == ans:
        ans = a
    else: continue
print(ans)
