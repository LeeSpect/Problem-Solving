import sys
input=sys.stdin.readline

t=int(input())
l=list(map(int,input().split()))

ansl=[l[0],l[1],l[2]]

for i in range(t-1):
    l = list(map(int,input().split()))
    pos = [0,0,0]
    for j in range(3):
        if j == 0:
            k = min([ansl[1], ansl[2]])
        elif j == 1:
            k = min([ansl[0], ansl[2]])
        else:
            k = min([ansl[0], ansl[1]])
        pos[j] = k+l[j]
    ansl = pos[:]
print(min(ansl))