import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if (a / b) < (3.14 * c * c / d):
            print('Whole pizza')
        else:
            print('Slice of pizza')        

if __name__ == '__main__':
    main()
