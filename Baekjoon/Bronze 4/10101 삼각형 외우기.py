L = [int(input()) for i in range(3)]
if sum(L) == 180:
    if min(L) == max(L):
        print('Equilateral')
    elif L[0]==L[1] or L[1]==L[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
