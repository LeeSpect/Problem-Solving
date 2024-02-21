import sys

n = sys.stdin.readline().rstrip()
ans=0
for i in range(len(n)):
    ans += int(n[i])**5
print(ans)
