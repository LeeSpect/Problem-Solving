import sys; input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())
    com = b/a
    print(int(com*3*c))

if __name__=='__main__':
    main()
