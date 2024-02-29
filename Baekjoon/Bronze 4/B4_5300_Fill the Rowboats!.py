import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(1, n+1):
        if (i-1)%6 == 0 and i != 1:
            print('Go!', end = ' ')
        print(i, end = ' ')
    print('Go!')

if __name__=='__main__':
    main()
