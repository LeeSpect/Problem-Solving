import sys; input = sys.stdin.readline

def main():
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = input().rstrip()
    i = 0
    ans = ''
    while 1:
        try:
            ans += string[i]
            i += ALPHA.index(string[i])+1
        except:
            print(ans)
            break

if __name__ == '__main__':
    main()
