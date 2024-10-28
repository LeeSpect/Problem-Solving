import sys
input = sys.stdin.readline

def main():
    n = int(input())
    print('V' * (n//5), end='')
    print('I' * (n%5))

if __name__ == '__main__':
    main()
