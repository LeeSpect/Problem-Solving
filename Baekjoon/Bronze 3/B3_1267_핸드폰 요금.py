n = int(input())
l = list(map(int, input().split()))
y,m = [],[]
for i in range(len(l)):
    y.append((l[i]//30+1)*10)
    m.append((l[i]//60+1)*15)
ys,ms = sum(y), sum(m)
if ys == ms: print(f'Y M {ys}')
elif ys > ms:
    print(f'M {ms}')
else: print(f'Y {ys}')
