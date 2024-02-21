l = [int(input()) for i in range(5)]
cnt = 0
while True:
    if l[0] == l[1]:
        print(cnt)
        break
    elif l[0] < 0:
        l[0] += 1
        cnt += l[2]
        continue
    elif l[0] == 0:
        cnt += l[3]+l[4]
        l[0] += 1
        continue
    else:
        l[0] += 1
        cnt += l[4]
