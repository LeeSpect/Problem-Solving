L = list(map(int, input().split()))
ans = 0
for i in L:
    ans += i*i
print(ans%10)
