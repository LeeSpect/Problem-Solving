l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ans = 0

for  i in range(3):
    if l2[i] < l[i]:
        continue
    else:
        ans += l2[i]-l[i]
print(ans)
