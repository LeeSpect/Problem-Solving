PIE = 3.1415927
i = 0
while True:
    i += 1
    d,r,t = map(float, input().split())
    if r == 0: break
    Perimeter = PIE*d
    distance = (Perimeter * r)/12/5280
    a = 3600/t
    mph = distance * a
    print(f'Trip #{i}: {distance:.2f} {mph:.2f}')
