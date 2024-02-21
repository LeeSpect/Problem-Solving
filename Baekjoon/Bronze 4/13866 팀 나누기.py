l = list(map(int, input().split()))
a = l.pop(l.index(max(l))) + l.pop(l.index(min(l)))
print(abs(sum(l)-a))
