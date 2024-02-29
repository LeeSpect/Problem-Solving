import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        l = list(map(int, input().split()))
        zack, mack = 0, 0
        if 18 in l:
            mack = 1
        if 17 in l:
            zack = 1
        print(*l)
        if mack and zack:
            print('both')
        elif mack:
            print('mack')
        elif zack:
            print('zack')
        else:
            print('none')
        print()

if __name__=='__main__':
    main()
