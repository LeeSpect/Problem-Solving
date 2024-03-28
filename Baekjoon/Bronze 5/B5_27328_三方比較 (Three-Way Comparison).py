import sys
input = sys.stdin.readline

def main():
    A = int(input())
    B = int(input())
    if A < B:
        print(-1)
    elif A == B:
        print(0)
    else:
        print(1)        

if __name__ == '__main__':
    main()
