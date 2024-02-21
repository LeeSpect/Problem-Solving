mc = 0
c = 0
for _ in range(10):
    a,b = map(int, input().split())
    c += b-a
    if mc < c:
        mc = c
print(mc)
