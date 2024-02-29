# 틀린 코드
import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    while 1:
        name = input()
        ans = ''
        for c in name:
            if c == 'e':
                ans += 'i'
            elif c == 'i':
                ans += 'e'
            else:
                ans += c
        print(ans)

if __name__=='__main__':
    main()
# ----------------------------------------------------------------------------------------------------
# 수정 코드: 뭐가 틀렸는지 모르겠음
def main():
    while 1:
        try:
            name = input()
            ans = ''
            for c in name:
                if c == 'e':
                    ans += 'i'
                elif c == 'i':
                    ans += 'e'
                elif c == 'I':
                    ans += 'E'
                elif c == 'E':
                    ans += 'I'
                else:
                    ans += c
            print(ans)
        except:
            break

if __name__ == '__main__':
    main()
