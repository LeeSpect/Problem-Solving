import sys; input = sys. stdin.readline

while 1:
    x, y = map(float, input().split())
    if not x or not y:
        print('AXIS')
    elif x > 0 and y > 0:
        print('Q1')
    elif x > 0 and y < 0:
        print('Q4')
    elif x < 0 and y < 0:
        print('Q3')
    else:
        print('Q2')

    if x == y == 0:
        break
