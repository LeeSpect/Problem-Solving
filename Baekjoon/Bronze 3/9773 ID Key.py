import sys; input = sys. stdin.readline

N = int(input())
for _ in range(N):
    string = input().rstrip()
    temp1 = 0
    for i in string:
        temp1 += int(i)
    temp2 = int(string[-3:]) * 10
    temp3 = temp1 + temp2
    if temp3 > 9999:
        print(str(temp3)[-4:])
    elif temp3 < 1000:
        print(temp3 + 1000)
    else:
        print(temp3)
