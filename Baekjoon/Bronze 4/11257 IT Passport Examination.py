import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        n, s, it, t = map(int, input().split())
        total = sum([s,it,t])
        print(n, total, end=' ')
        if total >= 55 and s >= 3.5*3 and it >= 2.5*3 and t >= 4*3:
            print('PASS')
        else:
            print('FAIL')

if __name__=='__main__':
    main()
