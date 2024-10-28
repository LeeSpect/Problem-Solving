import sys
input = sys.stdin.readline

def main():
    T = int(input())
    
    for i in range(1, T + 1):
        Gs = list(map(int, input().split()))
        Ss = list(map(int, input().split()))
        G_scoreboard, S_scoreboard = (1, 2, 3, 3, 4, 10), (1, 2, 2, 2, 3, 5, 10)
        G_score, S_score = 0, 0
        
        for j in range(6):
            G_score += Gs[j] * G_scoreboard[j]
            S_score += Ss[j] * S_scoreboard[j]
        S_score += Ss[6] * S_scoreboard[6]
        
        print(f'Battle {i}:', end=' ')
        
        if G_score > S_score:
            print('Good triumphs over Evil')
        elif G_score < S_score:
            print('Evil eradicates all trace of Good')
        else:
            print('No victor on this battle field')

if __name__ == '__main__':
    main()
