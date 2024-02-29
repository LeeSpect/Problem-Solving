import sys; input = sys.stdin.readline

def main():
    l = list(input().split())
    if int(l[0]) + int(l[2]) == int(l[4]):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
