import sys; input=sys.stdin.readline

def main():
    x, y = map(int, input().split())
    if y < x:
        print(y+x)
    else:
        print(y-x)

if __name__=='__main__':
    main()
