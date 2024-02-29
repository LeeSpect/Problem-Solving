import sys; input = sys.stdin.readline

def main():
    L = list(input().rstrip())
    l = len(L)
    A_score, B_score = 0, 0
    for i in range(0,l-1,2):
        if L[i+1] == '1':
            score = 1
        else:
            score = 2
        if L[i] == 'A':
            A_score += score
        else:
            B_score += score
        if abs(A_score - B_score) > 1 and (A_score >= 11 or B_score >= 11):
            if A_score > B_score:
                print('A')
            else:
                print('B')
            break

if __name__=='__main__':
    main()
