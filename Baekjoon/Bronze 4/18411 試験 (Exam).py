l = list(map(int, input().split()))
print(l.pop(l.index(max(l)))+l.pop(l.index(max(l))))
