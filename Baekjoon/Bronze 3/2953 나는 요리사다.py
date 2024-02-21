data = []
for _ in range(5):
    point = list(map(int, input().split()))
    data.append(sum(point))
print(data.index(max(data))+1, max(data))
