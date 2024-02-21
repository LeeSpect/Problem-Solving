# 틀린 코드: 문제를 잘못 읽고 마지막 digit만 고려하였다.
import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        n = input().rstrip()
        if n[-1] in ['1', '5', '6', '0']:
            print('YES')
        else:
            print('NO')

if __name__=='__main__':
    main()
    
# ----------------------------------------------------------------------------------------------------
# 수정 코드
import sys
input=sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = input().rstrip()
        len_n = len(n)
        test_case = str((int(n)**2) % (10**len_n))
        print('YES' if n == test_case else 'NO')

if __name__=='__main__':
    main()
