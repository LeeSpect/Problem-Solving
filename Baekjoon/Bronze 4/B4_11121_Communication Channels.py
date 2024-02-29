# 틀린 코드
import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        print('OK' if a==b else 'ERROR')

if __name__=='__main__':
    main()
    
# ---------------------------------------------------------------------------------
# 수정 코드: a가 b의 신호가 똑같거나 b의 각 부호를 반대로 한 신호와 똑같을 때 OK를 출력한다.
import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        a, b = map(str, input().split())
        leng_b = len(b)
        b2 = ''
        for j in range(leng_b):
            if b[j] == '0':
                b2 += '1'
            else:
                b2 += '0'
        if a==b or a==b2:
            print('OK')
        else:
            print('ERROR')

if __name__=='__main__':
    main()
