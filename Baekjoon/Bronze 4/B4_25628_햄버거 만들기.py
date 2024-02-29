import sys; input=sys.stdin.readline

def main():
    a, b = map(int, input().split())
    a //= 2
    print(min(a,b))

if __name__=='__main__':
    main()
