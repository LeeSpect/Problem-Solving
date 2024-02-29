import sys
input = sys.stdin.readline

d_s, y_s = map(int, input().split())
d_m, y_m = map(int, input().split())

d_s, d_m = -d_s, -d_m

while d_s != d_m:
    if d_s < d_m:
        d_s += y_s
    else:
        d_m += y_m

print(d_s)
