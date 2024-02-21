import sys; input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        print(' @@@   @@@ ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('@   @ @   @', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('@    @    @', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('@         @', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print(' @       @ ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('  @     @  ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('   @   @   ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('    @ @    ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()
    for i in range(n):
        print('     @     ', end = '')
        if i != n-1:
            print(' ', end = '')
    print()

if __name__ == '__main__':
    main()
