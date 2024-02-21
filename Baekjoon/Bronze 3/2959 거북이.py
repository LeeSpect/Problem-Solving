data = list(map(int, input().split()))
data.pop(data.index(max(data)))
print(max(data)*min(data))
