l = list(map(int, input().split()))
m = l.pop(l.index(max(l)))
print(2*m-sum(l))
