import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()) - 1)
print(sum(data)+1)
