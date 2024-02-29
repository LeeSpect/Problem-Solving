L = list(map(int, input().split()))
m = L.pop(L.index(max(L)))
if sum(L) > m or L[0]==L[1]==L[2]:
    print(1)
else:
    print(0)
