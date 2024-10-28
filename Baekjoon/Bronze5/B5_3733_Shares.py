import sys; input=sys.stdin.readline

def main():
    while 1:
        try:
            N,S=map(int,input().split())
            print(S//(N+1))
        except:
            break

if __name__=='__main__':
    main()
