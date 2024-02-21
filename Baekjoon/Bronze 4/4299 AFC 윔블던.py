x,y = map(int, input().split())
a = (x+y)/2; b = x-a
if (x+y)%2 == 0 and x>=y:
    print(int(a), int(b))
else:
    print(-1)

# 2A = x+y
