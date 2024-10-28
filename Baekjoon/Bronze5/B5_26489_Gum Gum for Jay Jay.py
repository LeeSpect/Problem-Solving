import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    result = 0
    while 1:
        s = input()
        if not s:
            break
        result += 1
    print(result)

if __name__=='__main__':
    main()
