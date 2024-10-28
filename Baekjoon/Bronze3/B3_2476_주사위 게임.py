import sys

n = int(sys.stdin.readline())
point_list = []
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == l[1] == l[2]:
        point_list.append(10000+l[0]*1000)
        continue
    elif l[0] == l[1] or l[0] == l[2]:
        point_list.append(1000+l[0]*100)
        continue
    elif l[1] == l[2]:
        point_list.append(1000+l[1]*100)
        continue
    else:
        point_list.append(100*max(l))

print(max(point_list))
