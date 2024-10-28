import sys; input=sys.stdin.readline

def main():
    l = list(map(int, input().split()))
    l.sort()
    C = l.pop()
    B = l.pop()
    A = l.pop()
    string = input().rstrip()
    for i in range(3):
        if string[i] == 'A':
            print(A, end=' ')
        elif string[i] == 'B':
            print(B, end=' ')
        else:
            print(C, end=' ')

if __name__=='__main__':
    main()
