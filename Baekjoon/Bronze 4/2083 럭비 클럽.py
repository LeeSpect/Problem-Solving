import sys; input=sys.stdin.readline

def main():
    while 1:
        name, age, weight = map(str, input().split())
        if name == '#' and age == weight == '0':
            break
        if int(age) > 17 or int(weight) >= 80:
            print(f'{name} Senior')
        else:
            print(f'{name} Junior')

if __name__=='__main__':
    main()
