import sys; input=sys.stdin.readline

def main():
    N = int(input())
    for i in range(N):
        string = input().rstrip()
        if 5 < len(string) < 10:
            print('yes')
        else:
            print('no')

if __name__=='__main__':
    main()
