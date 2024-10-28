l = [int(input()) for i in range(4)]
if (l[0] == 8 or l[0] == 9) and (l[3] == 8 or l[3] == 9) and l[1] == l[2]:
    print('ignore')
else:
    print('answer')
