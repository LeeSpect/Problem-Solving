n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    l2 = []
    for i in l:
        if i%2 == 0:
            l2.append(i)
    print(sum(l2), min(l2))
