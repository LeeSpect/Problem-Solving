import sys; input=sys.stdin.readline

def main():
    al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    N=int(input())
    for _ in range(N):
        string,number=map(str,input().split('-'))

        len_string=len(string)
        string_num=0
        for i in range(len_string):
            string_num+=al.index(string[i])*26**(len_string-1-i)
        number=int(number)
        if abs(string_num-number)<=100:
            print('nice')
        else:
            print('not nice')

if __name__=='__main__':
    main()
