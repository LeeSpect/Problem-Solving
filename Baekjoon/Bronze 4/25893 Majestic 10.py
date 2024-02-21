import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        cnt = 0
        if a >= 10:
            cnt += 1
        if b >= 10:
            cnt += 1
        if c >= 10:
            cnt += 1
        print(a, b, c)
        if cnt == 3:
            print('triple-double')
        elif cnt == 2:
            print('double-double')
        elif cnt == 1:
            print('double')
        else:
            print('zilch')
        print()

if __name__=='__main__':
    main()
