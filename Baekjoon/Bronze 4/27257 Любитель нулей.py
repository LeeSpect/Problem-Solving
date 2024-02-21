import sys; input = sys.stdin.readline

def main():
    string = int(input())
    string = str(string).rstrip('0')
    print(string.count('0'))

if __name__ == '__main__':
    main()
