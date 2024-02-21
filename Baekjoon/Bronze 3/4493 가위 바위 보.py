t = int(input())
for _ in range(t):
    n = int(input())
    a_score, b_score = 0,0

    for i in range(n):
        a,b = map(str, input().split())
        if a == 'R':
            if b == 'P': b_score += 1
            elif b == 'S': a_score += 1
        elif a == 'P':
            if b == 'R': a_score += 1
            elif b == 'S': b_score += 1
        else:
            if b == 'P': a_score += 1
            elif b == 'R': b_score += 1

    if a_score > b_score:
        print('Player 1')
    elif a_score < b_score:
        print('Player 2')
    else: print('TIE')
