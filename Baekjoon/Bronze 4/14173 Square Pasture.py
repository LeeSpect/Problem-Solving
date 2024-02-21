x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())

lx = [x1,x2,x3,x4]; ly = [y1,y2,y3,y4]
print((max(lx)-min(lx))**2 if max(lx)-min(lx) >= max(ly)-min(ly) else (max(ly)-min(ly))**2)
