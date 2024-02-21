H, M = map(int, input().split())

M = M-45

if M < 0:
    M = 60+M
    H -= 1
    if H == -1:
        H = 23

print(H, M)
