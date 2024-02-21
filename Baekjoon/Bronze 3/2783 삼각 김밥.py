x,y = map(int, input().split())
n = int(input())
data = [x/y]
for _ in range(n):
    x1,y1 = map(int, input().split())
    data.append(x1/y1)
print(f'{min(data)*1000:.2f}')
