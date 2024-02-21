import sys; input = sys.stdin.readline

def main():
    ALPHA = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    l = input().rstrip()
    for i in l:
        ALPHA.remove(i)
    print(ALPHA[0])

if __name__ == '__main__':
    main()
