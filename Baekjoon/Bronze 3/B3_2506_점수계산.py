n = int(input())
l = list(map(int, input().split()))
c = 0; p = 0
for i in range(n):
    if l[i] == 1:
        c += 1
        p += c
    else:
        c = 0
print(p)
