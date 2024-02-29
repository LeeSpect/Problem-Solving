# 틀린 코드
a,b,c = map(int, input().split(':'))
x,y,z = map(int, input().split(':'))

if z >= c: c = z-c
else:
    c = 60 - c + z
    y -= 1
if y >= b: b = y-b
else:
    b = 60 - b + y
    x -= 1
if x >= a: a = x-a
else:
    a = 24 - a + x
print(f'{a:0>2}:{b:0>2}:{c:0>2}')

# ------------------------------------------------------------------------------------------
# 수정 코드
a,b,c = map(int, input().split(':'))
x,y,z = map(int, input().split(':'))

if a == x and b == y and c == z:
    print('24:00:00')
else:
    if z >= c: c = z-c
    else:
        c = 60 - c + z
        y -= 1
    if y >= b: b = y-b
    else:
        b = 60 - b + y
        x -= 1
    if x >= a: a = x-a
    else:
        a = 24 - a + x
    print(f'{a:0>2}:{b:0>2}:{c:0>2}')
