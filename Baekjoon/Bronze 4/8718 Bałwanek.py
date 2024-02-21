# x리터의 눈이 내림
# k리터의 눈으로 공을 만들었음
x,k = map(int, input().split())
if k+k*2+k*4 <= x:
    print((k+k*2+k*4)*1000)
elif k+k*2+k/2 <= x:
    print(int(k+k*2+k/2)*1000)
elif k+k/2+k/4 <= x:
    print(int(k+k/2+k/4)*1000)
else:
    print(0)
