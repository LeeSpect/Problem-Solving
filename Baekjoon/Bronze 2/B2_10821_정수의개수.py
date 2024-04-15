import sys
input = sys.stdin.readline

numbers = list(map(str, input().rstrip().split(',')))

cnt = 0
for num in numbers:
    if str.isdigit(num):
        cnt += 1
print(cnt)
