import sys; input = sys.stdin.readline

def main():
    X = int(input())
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        X -= a*b
    if X == 0:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()
