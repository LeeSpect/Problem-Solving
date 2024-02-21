import sys
input = sys.stdin.readline

def main():

    s = input().rstrip()
    print(1 if s[0] == s[1] else 0)

if __name__ == '__main__':
    main()
