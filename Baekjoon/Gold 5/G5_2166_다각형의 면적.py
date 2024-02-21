# 틀린 코드: abs 함수를 잘못된 위치에 놓았다.
import sys; input=sys.stdin.readline

def main():
    N=int(input())
    dots=[tuple(map(int,input().split())) for _ in range(N)]
    area=0
    x1,y1=dots[0]
    for i in range(1,N-1):
        x2,y2=dots[i]; x3,y3=dots[i+1]
        area+=0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1))
    print(f'{area:0.1f}')

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# 수정 코드: abs함수와 *0.5를 뒤로 빼서, 출력 직전에 적용되도록 하였다.
import sys; input=sys.stdin.readline

def main():
    N=int(input())
    dots=[tuple(map(int,input().split())) for _ in range(N)]
    area=0
    x1,y1=dots[0]
    for i in range(1,N-1):
        x2,y2=dots[i]; x3,y3=dots[i+1]
        area+=(x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1)
    print(f'{abs(area)*0.5:0.1f}')

if __name__=='__main__':
    main()

# 다각형은 삼각형으로 분해할 수 있다.
# 다각형을 구성하는 임의의 한 점 a를 지정한다.
# 점 a와 다른 임의의 두 점 b, c를 이어서 만들 수 있는 서로 다른 삼각형의 모든 넓이를 더한다.
# 삼각형의 세 점의 좌표가 a(x1,y1), b(x2,y2), c(x3,y3)라고 할 때, 삼각형의 넓이는 0.5 * abs((x1*xy2 + x2*y3 + x3*y1) - (x1*y3 + x3*y2 + x2*y1))이다. 
