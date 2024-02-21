a1,p1 = map(int, input().split())
r1,p2 = map(int, input().split())

print('Whole pizza' if a1/p1 < ((r1**2)*3.1415926535897)/p2 else 'Slice of pizza')    
