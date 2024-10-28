for i in range(3):
    L = list(map(int, input().split()))
    a = L[3]-L[0]
    if L[4]-L[1] < 0:
        a -= 1
        b = 60+(L[4]-L[1])
    else:
        b = L[4]-L[1]
    if L[5]-L[2] < 0:
        b -= 1
        if b == -1:
            b += 60
            a -= 1
        c = 60+(L[5]-L[2])
    else:
        c = L[5]-L[2]
    print(a, b, c)
