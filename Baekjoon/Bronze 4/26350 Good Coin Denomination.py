import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        l = list(map(int, input().split()))
        print('Denominations:', *l[1:])
        flag = 1
        for c in range(2, l[0]+1):
            if l[c] < l[c-1]*2:
                flag = 0
                break
        if flag:
            print('Good coin denominations!')
        else:
            print('Bad coin denominations!')
        print()

if __name__ == '__main__':
    main()
