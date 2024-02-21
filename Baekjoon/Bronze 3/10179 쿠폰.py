import sys

n = int(sys.stdin.readline())
data = [float(sys.stdin.readline().strip()) for i in range(n)]
for i in range(n):
    print(f"${data[i]*80/100:0.2f}")
