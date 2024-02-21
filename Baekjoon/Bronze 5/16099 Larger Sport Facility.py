import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        l1, w1, l2, w2 = map(int, input().split())
        ans1, ans2 = l1*w1, l2*w2
        if ans1 > ans2:
            print('TelecomParisTech')
        elif ans1 < ans2:
            print('Eurecom')
        else:
            print('Tie')

if __name__=='__main__':
    main()
