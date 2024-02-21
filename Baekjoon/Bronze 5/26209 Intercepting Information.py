import sys; input = sys.stdin.readline

def main():
    l = list(map(int, input().split()))
    for e in l:
        if e not in [0, 1]:
            print('F')
            exit()
    print('S')

if __name__=='__main__':
    main()
