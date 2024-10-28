import sys; input=sys.stdin.readline

def main():
    T = int(input())
    for i in range(1,T+1):
        string = input().rstrip()
        print(f'{i}. {string}')

if __name__=='__main__':
    main()
