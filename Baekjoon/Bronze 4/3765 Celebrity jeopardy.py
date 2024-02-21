# 수정 코드: 수정 코드: sys 쓰면 출력초과가 발생한다.

def main():
    while 1:
        try:
            a = input()
            print(a)
        except:
            break

if __name__=='__main__':
    main()
