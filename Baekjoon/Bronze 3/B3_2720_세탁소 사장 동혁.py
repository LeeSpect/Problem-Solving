t = int(input())
for _ in range(t):
    n = int(input())
    q = n//25; n -= q*25
    d = n//10; n -= d*10
    k = n//5; n -= k*5
    print(q, d, k, n)
