import sys; input = sys.stdin.readline

def main():
    string = input().rstrip()
    A, B = 0, 0
    for i in string:
        if i == 'A':
            A += 1
        else:
            B += 1
    print(A, ':', B)

if __name__ == '__main__':
    main()
