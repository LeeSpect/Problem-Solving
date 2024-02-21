import sys; input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(T):
        string, a, b = map(str, input().split())
        print(string[:int(a)] + string[int(b):])

if __name__ == '__main__':
    main()
