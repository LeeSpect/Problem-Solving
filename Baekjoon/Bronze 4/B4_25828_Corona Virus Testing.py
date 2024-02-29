import sys; input=sys.stdin.readline

def main():
    g, p, t = map(int, input().split())
    e1 = g * p
    e2 = g + p * t
    if e1 == e2:
        print(0)
    elif e1 < e2:
        print(1)
    else:
        print(2)

if __name__=='__main__':
    main()
