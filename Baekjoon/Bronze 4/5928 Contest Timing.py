D,H,M = map(int, input().split())
d1,h1,m1 = 11,11,11

DD = M+60*H+24*60*D
dd = 11+11*60+11*24*60

if DD-dd < 0:
    print(-1)
else:
    print(DD-dd)
